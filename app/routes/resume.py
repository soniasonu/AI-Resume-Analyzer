import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.services.pdf_service import extract_text_from_pdf
from app.services.ai_service import analyze_resume
from flask import Blueprint, render_template, request, flash, redirect, url_for

from app import db
from app.models.resume import Resume
import json
from app.models.analysis import Analysis

resume = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf"}

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@resume.route("/upload", methods=["GET", "POST"])
@login_required
def upload_resume():

    if request.method == "POST":

        file = request.files["resume"]
        job_role = request.form["job_role"]

        if not allowed_file(file.filename):
            flash("Only PDF files are allowed.", "danger")
            return redirect(url_for("resume.upload_resume"))
        

        if file.filename == "":
            flash("Please select a PDF file.", "danger")
            return redirect(url_for("resume.upload_resume"))

        filename = secure_filename(file.filename)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # Save uploaded PDF
        file.save(filepath)

        # Extract text
        resume_text = extract_text_from_pdf(filepath)

        # Analyze with AI
        analysis = analyze_resume(resume_text, job_role)

        # Save Resume to database FIRST
        resume = Resume(
            filename=filename,
            filepath=filepath,
            job_role=job_role,
            user_id=current_user.id
        )

        db.session.add(resume)
        db.session.commit()

        # Save Analysis
        saved_analysis = Analysis(
            summary=analysis["summary"],
            missing_skills=json.dumps(analysis["missing_skills"]),
            interview_questions=json.dumps(analysis["interview_questions"]),
            learning_roadmap=json.dumps(analysis["learning_roadmap"]),
            project_ideas=json.dumps(analysis["project_ideas"]),
            resume_id=resume.id
        )

        db.session.add(saved_analysis)
        db.session.commit()

        return render_template(
            "analysis.html",
            analysis=analysis
        )

    return render_template("upload_resume.html")

@resume.route("/analysis/<int:analysis_id>")
@login_required
def view_analysis(analysis_id):

    analysis = Analysis.query.get_or_404(analysis_id)

    return render_template(
        "analysis.html",
        analysis={
            "summary": analysis.summary,
            "missing_skills": json.loads(analysis.missing_skills),
            "interview_questions": json.loads(analysis.interview_questions),
            "learning_roadmap": json.loads(analysis.learning_roadmap),
            "project_ideas": json.loads(analysis.project_ideas),
        }
    )

@resume.route("/delete/<int:resume_id>", methods=["POST"])
@login_required
def delete_resume(resume_id):
    resume = Resume.query.get_or_404(resume_id)

    # Security: only allow the owner to delete
    if resume.user_id != current_user.id:
        flash("You are not authorized to delete this resume.", "danger")
        return redirect(url_for("main.dashboard"))

    # Delete PDF file from uploads folder
    if os.path.exists(resume.filepath):
        os.remove(resume.filepath)

    # Delete database record
    db.session.delete(resume)
    db.session.commit()

    flash("Resume deleted successfully!", "success")
    return redirect(url_for("main.dashboard"))
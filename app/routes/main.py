from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.resume import Resume

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")


@main.route("/dashboard")
@login_required
def dashboard():

    resumes = Resume.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "dashboard.html",
        resumes=resumes
    )
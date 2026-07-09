from app import db

class Analysis(db.Model):
    __tablename__ = "analyses"

    id = db.Column(db.Integer, primary_key=True)

    summary = db.Column(db.Text, nullable=False)

    missing_skills = db.Column(db.Text, nullable=False)

    interview_questions = db.Column(db.Text, nullable=False)

    learning_roadmap = db.Column(db.Text, nullable=False)

    project_ideas = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    resume_id = db.Column(
        db.Integer,
        db.ForeignKey("resumes.id"),
        nullable=False
    )
from flask import Blueprint, render_template, request, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user

from flask_login import login_user, logout_user

from app import db
from app.models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered."

        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("main.home"))

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("main.dashboard"))
        return "Invalid email or password."
    return render_template("login.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
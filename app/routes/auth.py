from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from app import db
from app.models.user import User


auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
         username = request.form["username"]
         email = request.form["email"]
         password = request.form["password"]

         new_user = User(
              username = username,
              email = email,
              password_hash=generate_password_hash(password)
         )

         db.session.add(new_user)
         db.session.commit()

         return redirect(url_for("main.home"))
    return render_template("register.html")
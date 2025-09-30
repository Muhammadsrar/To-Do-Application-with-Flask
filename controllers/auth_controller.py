from flask import Blueprint, request, jsonify, redirect, url_for, render_template, make_response,session
from models.user import User
from models.task import Task
import jwt,datetime

SECRET_KEY = "your_secret_key_here"

auth_bp = Blueprint("auth", __name__)
#SECRET_KEY = "your_secret_key_here"

# ---------------- Register Page (GET) ----------------
@auth_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

# ---------------- Signup ----------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.form

    # username aur password required
    if not data.get("name") or not data.get("password") or not data.get("email"):
        return "Error: Username and password and email are required", 400

    # duplicate user check
    if User.objects(username=data.get("name")).first():
        return "Error: User already exists", 400

    # new user create
    user = User(username=data.get("name"), email=data.get("email"))
    user.set_password(data.get("password"))
    user.save()

    return redirect(url_for("auth.login_page"))

# ---------------- Login Page (GET) ----------------
@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


  # ---------------- Login ----------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.form
    
        # Required fields check sabse pehle
    if not data.get("name") or not data.get("password"):
        return "Error: Username and password are required", 400

    user = User.objects(username=data.get("name")).first()
    if not user or not user.check_password(data.get("password")):
       return "invalid user name or password"

         # token generate
    token = jwt.encode({
        "user_id": str(user.id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")

    # cookie me token set
    resp = make_response(redirect(url_for("tasks.dashboard")))
    resp.set_cookie("token", token)
    return resp

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
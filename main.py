from flask import Flask,render_template
from mongoengine import connect
from controllers.auth_controller import auth_bp
from controllers.task_controller import task_bp

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
connect(
    db="task_manager",              
    host="localhost",
    port=27017
)

@app.route('/')
def home():
    return render_template("home.html")

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(task_bp, url_prefix="/tasks")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
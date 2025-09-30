from flask import Blueprint, request,jsonify,render_template,redirect,url_for
from models.task import Task
from datetime import datetime
from controllers.auth_decorator import token_required



task_bp = Blueprint("tasks", __name__)

# ---------------- Create Task ----------------
@task_bp.route("/create", methods=["POST"])
@token_required
def create_task(current_user):
    # form-data se values lena
    title = request.form.get("title")
    description = request.form.get("description")
    deadline_str = request.form.get("deadline")
    category = request.form.get("category")

    # required fields check
    if not title or not description or not deadline_str or not category:
        return "error Missing fields"

    # category validation
    allowed_categories = ["Personal", "Office"]
    if category not in allowed_categories:
        return "error Invalid category "
        

    # deadline validate
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    except ValueError:
        return "error Invalid deadline  YYYY-MM-DD"

    # create duplicate  task for same user
    existing_task = Task.objects(name=current_user.username, title=title).first()
    if existing_task:
        return "Error: You already have a task with this title."


    # new task create
    task = Task(
        name=current_user.username,
        title=title,
        description=description,
        deadline=deadline,
        category=category
    )
    task.save()

    return render_template(
    "task_create.html",
    task_id=task.id,
    category=task.category
), 201



# ---------------- Get Task by ID ----------------
@task_bp.route("/<task_id>", methods=["GET"])
@token_required
def get_task(current_user, task_id):
    task = Task.objects(id=task_id , name=current_user.username).first()
    if not task:
        return "Task not found", 404

    return f"""
    Task ID: {task.id} <br>
    Title: {task.title} <br>
    Description: {task.description} <br>
    Deadline: {task.deadline.strftime('%Y-%m-%d')} <br>
    Category: {task.category} <br>
    """

# ---------------- View All Tasks (Template) ----------------
@task_bp.route("/all", methods=["GET"])
@token_required
def get_all_tasks(current_user):
    tasks = Task.objects(name=current_user.username)
    return render_template("tasks.html", username=current_user.username, tasks=tasks)

 

# ---------------- Filter Tasks by Category ----------------
@task_bp.route("/filter", methods=["GET"])
@token_required
def filter_tasks(current_user):
    category = request.args.get("category")

    allowed_categories = ["Personal", "Office"]
    if not category or category not in allowed_categories:
        return "Invalid or missing category. Use Personal or Office", 400

    tasks = Task.objects(name=current_user.username, category=category)

    return render_template(
        "tasks.html",
        username=current_user.username,
        tasks=tasks,
        category=category
    )


# ---------------- Update Form Page ----------------
@task_bp.route("/update_form/<task_id>", methods=["GET"])
@token_required
def update_form(current_user, task_id):
    task = Task.objects(id=task_id, name=current_user.username).first()
    if not task:
        return "Task not found", 404
    return render_template("update_task.html", task=task)


# ---------------- Update Task (form submit) ----------------
@task_bp.route("/update/<task_id>", methods=["Put"])
@token_required
def update_task(current_user, task_id):
    task = Task.objects(id=task_id, name=current_user.username).first()
    if not task:
        return "Task not found", 404

    task.title = request.form.get("title", task.title)
    task.description = request.form.get("description", task.description)

    new_category = request.form.get("category")
    if new_category:
        allowed_categories = ["Personal", "Office"]
        if new_category not in allowed_categories:
            return "Invalid category. Use Personal or Office", 400
        task.category = new_category

    if request.form.get("deadline"):
        try:
            task.deadline = datetime.strptime(request.form.get("deadline"), "%Y-%m-%d")
        except ValueError:
            return "Invalid deadline format. Use YYYY-MM-DD", 400

    task.save()
    return redirect(url_for("tasks.get_all_tasks"))
    

# ---------------- Delete Task ----------------
@task_bp.route("/delete/<task_id>", methods=["POST"])
@token_required
def delete_task(current_user, task_id):
    task = Task.objects(id=task_id, name=current_user.username).first()  # Corrected
    if not task:
        return "Task not found ", 404

    task.delete()
    return "Task deleted successfully"


# ---------------- Dashboard Page ----------------
@task_bp.route("/dashboard", methods=["GET"])
@token_required
def dashboard(current_user):
    # Yaha pe tum template render kara sakte ho
    return render_template("dashboard.html", username=current_user.username)

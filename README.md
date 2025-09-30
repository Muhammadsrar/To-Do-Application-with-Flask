Flask To-Do Application

A simple and professional task management web app with user authentication, task creation, filtering, and frontend views. Built using Flask, MongoDB, and MongoEngine.

✅ Features

User Registration & Login

Create Tasks (Title, Description, Deadline)

Task Categories: Personal & Office

Edit & Delete Tasks

View All Tasks

Filter by Category

Frontend with HTML, CSS, Jinja2

✅ Tech Stack

Backend: Flask (Python)

Database: MongoDB

ODM: MongoEngine

Frontend: HTML, CSS Templates

✅ Main Routes
Action	Route
Register/Login	/register, /login
Dashboard	/tasks/dashboard
Create Task	/tasks/create
All Tasks	/tasks/all
Filter Tasks	`/tasks/filter?category=Personal
Update/Delete	/tasks/update/<id>, /tasks/delete/<id>
Logout	/auth/logout
✅ Installation
git clone <repo-url>
cd project-folder
pip install -r requirements.txt
flask run


Make sure MongoDB is running locally or update the connection string.

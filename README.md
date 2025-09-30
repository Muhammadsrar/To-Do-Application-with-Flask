# Flask To-Do Application

A simple and organized task management web application built using Flask, MongoDB, and MongoEngine. The application allows users to register, log in, and manage their personal and office tasks with a clean interface.

# Features

User authentication (signup and login)

Create, edit, and delete tasks

Task fields include:

Title

Description

Deadline

Category (Personal / Office)

Filter tasks by category

View all tasks in a dashboard

Frontend built using HTML, CSS, and Jinja2 templates

# Tech Stack

Backend: Flask (Python)
Database: MongoDB
ODM: MongoEngine
Frontend: HTML, CSS, Jinja2

# Routes Overview
Action	Route
Register / Login	/register, /login
Dashboard	/tasks/dashboard
Create Task	/tasks/create
View All Tasks	/tasks/all
Filter Tasks	/tasks/filter?category=Personal
Update Task	/tasks/update/<id>
Delete Task	/tasks/delete/<id>
Logout	/auth/logout
Getting Started
1. Clone the repository
git clone <repo-url>
cd project-folder

2. Install dependencies
pip install -r requirements.txt

3. Run the application
flask run

# Notes

Make sure MongoDB is running locally, or update the database connection string in the configuration.

The project follows a modular structure with separate files for routes, templates, and models.

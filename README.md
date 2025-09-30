Flask To-Do Application

A web-based task management system that allows users to register, log in, create and manage tasks with deadlines and categories. It is built using Flask, MongoDB, and MongoEngine, and includes both backend APIs and basic frontend pages using HTML/CSS.

✅ Features

User Authentication
Users can sign up and log in securely.

Task Management
Create tasks with:

Title

Description

Deadline

Category (Personal or Office)

Task Operations

Update existing tasks

Delete tasks

View all tasks

Category-Based Filtering
Users can filter tasks by:

Personal

Office

Frontend Support
Basic browser interface using HTML, CSS, and Jinja2.

✅ Technology Stack
Component	Technology Used
Backend	Flask (Python)
Database	MongoDB
ORM/ODM	MongoEngine
Frontend	HTML + CSS (Jinja2 Templates)
✅ API / Routes Overview
Feature	Endpoint / Route
User Register	/register
User Login	/login
Create Task	/tasks/create
All Tasks	/tasks/all
Update Task	/tasks/update/<task_id>
Delete Task	/tasks/delete/<task_id>
Filter Tasks	`/tasks/filter?category=Personal
Dashboard	/tasks/dashboard
Logout	/auth/logout
✅ Installation & Setup
✅ Prerequisites

Python 3.8+

MongoDB installed or access to MongoDB Atlas

pip installed

✅ Steps

Clone the Repository

git clone <repository-url>
cd <project-folder>


Create Virtual Environment

python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # Mac/Linux


Install Dependencies

pip install -r requirements.txt


Configure Database
Make sure MongoDB is running locally OR update your connection string in the code.

Run the Application

flask run


Access in Browser
👉 http://127.0.0.1:5000/

✅ Usage

Open the browser and go to the home page

Register or log in

Create tasks using the dashboard

View all tasks or filter by category

Update or delete tasks as needed

Logout safely

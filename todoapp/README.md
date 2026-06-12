# Django Todoapp Project

A simple Django Todo application with **CRUD functionality**, **user authentication&authorization**, **profile management**, **automated tests** and **task organization** by category, priority, and status. Built with PostgreSQL and Bootstrap 5, featuring a responsive sidebar UI with filtering, sorting, and avatar upload support.

---


## 📌 Features

- User authentication (login/logout/register)
- Management profile such as changing username, password and profile photo
- Create, read, update, delete (CRUD) tasks
- Author-only permissions for editing and deleting tasks
- Organizarion tasks with priority, category and status.
- Form validation and error handling
- Automated test suite using Django's built-in test framework

---

## 🛠 Tech Stack

- Python 
- Django 
- PostgreSQL
- Django Test Framework

---

⚙️ Setup Instructions
1️⃣ Clone the repository

bash

git clone https://github.com/amirhoseinsalami/DjangoProject

cd todoapp

2️⃣ Create a virtual environment

bash

python -m venv venv

source venv/bin/activate # Linux / macOS

venv\Scripts\activate # Windows

3️⃣ Install dependencies

bash

pip install django

4️⃣ Run migrations

bash

python manage.py migrate

5️⃣ Create a superuser (optional)

bash

python manage.py createsuperuser

6️⃣ Run the development server

bash

python manage.py runserver

Open your browser at:

http://127.0.0.1:8000/


🔐 Authentication & Authorization

    Users must be logged in to add tasks
    Only the author of a task can edit or delete it
    Unauthorized users are redirected to the login page or receive a permission error


✅ Running Tests
Run all tests:

bash

python manage.py test

Run tests for the tasks app:

bash

python manage.py test tasks

Run tests for the accounts app:

bash

python manage.py test accounts


Run a specific test class:

bash

python manage.py test tasks.tests.TestCRUD

Run a single test method:

bash

python manage.py test tasks.tests.TestCRUD.test_add_task


🧪 Test Coverage

The automated tests cover:
CRUD Logic

    Creating posts
    Reading posts
    Updating posts
    Deleting posts

Authorization

    Login required for protected views
    Author-only edit and delete permissions

Edge Cases

    Invalid form submissions
    Non-existent objects return 404
    Anonymous access protection

Registration

    Create user
    Redirect after successful registering

Login/Logout

    Valid mlogin
    Invalid login
    Logout

Profile

    Required login for profile page
    Update username/profile photo
    Delete profile photo

🔧 Configuration Notes
Login Redirect URL
LOGIN_URL
LOGOUT_REDIRECT_URL

Ensure the following setting exists in settings.py:

python

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'accounts:login'


---

🚀 Deployment Notes

    Set DEBUG = False in production
    Configure ALLOWED_HOSTS
    Use PostgreSQL or another production-grade database
    Collect static files before deployment:

bash

python manage.py collectstatic

👤 Author
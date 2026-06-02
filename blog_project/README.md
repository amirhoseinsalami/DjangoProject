# Django Blog Project ✅

A simple Django blog application with full **CRUD functionality**, **authentication**, **authorization**, and **automated tests** to prevent regressions.

---

## 📌 Features

- User authentication (login/logout)
- Create, read, update, delete (CRUD) blog posts
- Author-only permissions for editing and deleting posts
- Form validation and error handling
- Edge-case handling (404s, invalid input)
- Automated test suite using Django's built-in test framework

---

## 🛠 Tech Stack

- Python 3.10+
- Django 4.x
- PostgreSQL
- Django Test Framework

---

## 📂 Project Structure

blog_project/

│

├── manage.py

├── README.md

├── blog_project/

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

│ └── asgi.py

│

└── blog/

├── migrations/

├── templates/

│ └── blog/

├── models.py

├── views.py

├── urls.py

├── forms.py

├── tests.py

└── admin.py

│

└── accounts/

├── templates/

├── models.py

├── views.py

├── urls.py

├── tests.py

└── admin.py

│

└── resources/

├── static/

├── templates/



⚙️ Setup Instructions
1️⃣ Clone the repository

bash

git clone https://github.com/amirhoseinsalami/DjangoProject

cd django-blog

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

    Users must be logged in to create posts
    Only the author of a post can edit or delete it
    Unauthorized users are redirected to the login page or receive a permission error

✅ Running Tests
Run all tests:

bash

python manage.py test

Run tests for the blog app:

bash

python manage.py test blog

Run a specific test class:

bash

python manage.py test blog.tests.TestCRUD

Run a single test method:

bash

python manage.py test blog.tests.TestCRUD.test_create_post

Run tests with verbose output:

bash

python manage.py test -v 2

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

🔧 Configuration Notes
Login Redirect URL

Ensure the following setting exists in settings.py:

python

LOGIN_URL = 'login/'

🚀 Deployment Notes

    Set DEBUG = False in production
    Configure ALLOWED_HOSTS
    Use PostgreSQL or another production-grade database
    Collect static files before deployment:

bash

python manage.py collectstatic


🤝 Contributing

    Fork the repository
    Create a new feature branch
    Write tests for your changes
    Submit a pull request

👤 Author

Built with ❤️ using Django.

# Django To-Do App

This is a simple To-Do web application I built using Django. It lets users sign up, log in, and manage their tasks easily.

---

## Features

- User signup and login
- Add new tasks
- Edit tasks
- Mark tasks as completed
- Delete tasks
- Simple and clean interface

---

## Project Structure

```
project_folder/
│
├── todo_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── home.html
│   ├── static/
│   │   └── css/
│   │       ├── login.css
│   │       ├── signup.css
│   │       └── styles.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── requirements.txt
├── .gitignore
├── manage.py
└── README.md

```

---

## Setup

1. Clone the repo:
```bash
git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app
```

2. Create and activate a virtual environment:
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to see the app.



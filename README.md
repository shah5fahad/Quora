# Quora-Like Question & Answer Platform

A full-featured Question & Answer platform inspired by **Quora**, built using **Django 5.0.7** and **Python 3.12.4**. This application allows registered users to post questions, answer other users' questions (only once per question), and like answers.

---

## Features

- ✅ User registration, login, and logout (Django built-in user system)
- ✅ Authenticated users can:
  - Post new questions
  - View all questions
  - View question details and associated answers
  - Answer any question **once**
  - Like any answer
- ✅ Form validations using Django Forms
- ✅ Clean and responsive UI using Bootstrap 5
- ✅ Class-based views (CBVs) for all pages
- ✅ Secure login required for posting/answering
- ✅ Django Admin for managing users and content

---

## Tech Stack

| Tool         | Version    |
|--------------|------------|
| Python       | 3.12.4     |
| Django       | 5.0.7      |
| SQLite       | Default (for dev) |
| HTML/CSS     | Bootstrap 5 |
| JavaScript   | Vanilla JS |

------

## 📁 Project Structure
````bash
quora_project/
├── Posts/                          # App containing questions, answers
│   ├── models.py                   # Models: Question, Answer, Like
│   ├── views.py                    # CBVs: List, Detail, Create
│   ├── forms.py                    # Django forms for input
│   ├── urls.py                     # App URL patterns
│   ├── templates/
│   │   └── question_list.html
│   │   ├── question_detail.html
│   │   └── question_form.html
│
├── users/                          # User-related views and forms
│   ├── views.py                    # Login, Logout, Register (CBVs)
│   ├── forms.py                    # User signup form
│   ├── templates/
│   │   └── login.html
│   │   ├── logout.html
│   │   └── register.html
│
├── templates/
│   └── base.template                   # Bootstrap layout
│
├── Quora/
│   └── settings.py                 # Installed apps and middleware
│
├── manage.py
└── README.md
````
---

## Setup Instructions

1. **Clone the repository**
````bash
git clone https://github.com/your-username/quora-clone.git
cd quora-clone
````
2. **Create a virtual environment and activate it**
````bash
python3.12 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
````
3. **Install dependencies**
````bash
pip install -r requirements.txt
````
4. **Apply migrations**
````bash
python manage.py makemigrations
python manage.py migrate
````
5. **Create a superuser (for admin access)**
````bash
python manage.py createsuperuser
````
6. **Run the server**
````bash
python manage.py runserver
````
7. **Access the application**
````bash
Frontend: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/
````
## Forms Used

QuestionForm — For submitting a question (title & description)

AnswerForm — For answering questions (one per user per question)

UserRegistrationForm — For signing up users

Login — Using Django’s built-in AuthenticationForm


## Authentication

Only logged-in users can:

Post new questions

Answer questions

Like answers

LoginRequiredMixin is used to restrict access to views.

## Author
Built using Django by Shah Fahad
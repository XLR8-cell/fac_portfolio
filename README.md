# Django Personal Portfolio Website

A multi-page personal portfolio web application built with Python, Django, and Bootstrap 5 following the Django MVT (Model-View-Template) architecture.

## 🚀 Features & Architecture
- **5 Core Pages:** Home, About, Projects, Skills, and Contact.
- **Template Inheritance:** Modular HTML structure extending a shared `base.html` layout.
- **Bootstrap 5 UI:** Responsive layout with navigation bar and footer.
- **Global Context Processor:** Supplies shared site-wide metadata across all view templates.
- **Named URL Routing:** Modular, namespaced URL patterns using Django's `path()` routing.

## 📁 Project Structure
```text
fac_portfolio/
├── manage.py
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pages/
│   ├── views.py
│   ├── urls.py
│   └── context_processors.py
├── templates/
│   ├── base.html
│   └── pages/
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       ├── skills.html
│       └── contact.html
└── README.md
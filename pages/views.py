from django.shortcuts import render


# Create your views here.

def home(request):
    context = {
        'headline': 'Building Scalable Web Applications & Systems',
        'summary': 'Software Engineering student with a passion for robust backend architecture, clean API design, and modern web frameworks.',
        'featured_skills': ['Python', 'Django', 'React', 'REST APIs', 'PostgreSQL'],
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
        'bio': 'I am a Software Engineer based in Nairobi, Kenya. I specialize in building backend systems with Python/Django and interactive client interfaces with React. I enjoy exploring low-level system design, backend efficiency, and modern web standards.',
        'education': [
            {'degree': 'Software Engineering & Web Development', 'institution': 'FAC Academy', 'year': '2026'},
            {'degree': 'B.Sc. in Software Engineering / Computer Science', 'institution': 'University Partner', 'year': 'In Progress'},
        ],
        'highlights': [
            'Participant in Cybersecurity Defense & SOC Analyst Track',
            'Focus on full-stack application security and architecture',
        ]
    }
    return render(request, 'pages/about.html', context)

def projects(request):
    context = {
        'project_list': [
            {
                'title': 'Hospital Management System (HMS)',
                'tech': 'Python, OOP, SQLite',
                'description': 'A modular healthcare administration system handling patient records, appointments, and diagnostic billing workflows.',
                'status': 'Completed',
                'github': 'https://github.com',
            },
            {
                'title': 'Developer Portfolio Engine',
                'tech': 'Django, Bootstrap 5, MVT Architecture',
                'description': 'A multi-page dynamic portfolio featuring custom template inheritance, context processing, and clean URL routing.',
                'status': 'Active',
                'github': 'https://github.com',
            },
            {
                'title': 'Library Management Portal',
                'tech': 'Python, CSV Storage',
                'description': 'Lightweight record management app designed for fast data processing and offline storage handling.',
                'status': 'Completed',
                'github': 'https://github.com',
            },
        ]
    }
    return render(request, 'pages/projects.html', context)

def skills(request):
    context = {
        'skill_categories': {
            'Backend & Frameworks': ['Python 3', 'Django', 'REST Framework', 'SQL / SQLite'],
            'Frontend Development': ['JavaScript (ES6+)', 'React', 'Bootstrap 5', 'HTML5 / CSS3'],
            'Tools & Methods': ['Git & GitHub', 'Virtual Environments (venv/uv)', 'VS Code', 'MVT / MVC Architecture'],
            'Exploratory & Systems': ['COBOL Data Structure', 'Cybersecurity Defense Fundamentals'],
        }
    }
    return render(request, 'pages/skills.html', context)

def contact(request):
    context = {
        'location': 'Nairobi, Kenya',
        'availability': 'Open for software engineering internships, junior developer roles, and project collaborations.',
    }
    return render(request, 'pages/contact.html', context)
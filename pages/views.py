from django.shortcuts import render
from .models import Project, Skills


# Create your views here.

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    
    if not featured_projects.exists():
        # If no featured projects, get the latest 3 projects
       # featured_projects = Project.objects.all().order_by('-created_at')[:3]
        featured_projects = Project.objects.filter(is_featured=True)  # Convert to list for easier manipulation
        
    context = {
        'headline': 'Building Scalable Web Applications & Systems',
        'summary': 'A modern portfolio showcasing projects, technical skills and our journey as software developers.',
        'featured_skills': ['Python', 'Django', 'React', 'REST APIs', 'PostgreSQL'],
        'total_projects': Project.objects.count(),
        'total_skills': Skills.objects.count(),
        'featured_projects': featured_projects,
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
    projects = Project.objects.all().order_by('-id')
    context = {
        'projects': projects
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
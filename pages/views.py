from django.shortcuts import render
from .models import Project, Skills

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    
    # Fallback to the latest 3 projects if none are marked featured
    if not featured_projects.exists():
        featured_projects = Project.objects.all().order_by('-created_at')[:3]
        
    context = {
        'featured_skills': ['Python / Django', 'JavaScript / React', 'RESTful APIs', 'PostgreSQL', 'Git Workflow'],
        'total_projects': Project.objects.count(),
        'total_skills': Skills.objects.count(),  # Uses models.Skills
        'featured_projects': featured_projects,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
        'bio': 'We are a group of software engineering students collaborating on modern web applications, backend system design, and scalable full-stack architectures using Python and Django.',
        'team_members': [
            {'name': 'Benard Shikhule', 'role': 'Backend & Architecture'},
            {'name': 'Gilbert Nyamberi', 'role': 'Frontend & Integration'},
            {'name': 'Vennesa Njuguna', 'role': 'UI/UX, QA & Version Control'},
            {'name': 'June Siele', 'role': 'QA & Version Control'},
        ],
        'highlights': [
            'Collaborative Git workflow utilizing feature branches and Pull Requests',
            'Full-stack MVT architecture built with secure Django components',
            'Focus on system design, database optimization, and application security',
        ],
        'education': [
            {'degree': 'Software Engineering & Web Development', 'institution': 'FAC Academy', 'year': '2026'},
            {'degree': 'B.Sc. Computer Science / Software Engineering', 'institution': 'Partner University', 'year': 'In Progress'},
        ]
    }
    return render(request, 'pages/about.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all().order_by('-id'),
    }
    return render(request, 'pages/projects.html', context)

def skills(request):
    context = {
        'skill_categories': {
            'Backend & Core Frameworks': ['Python 3', 'Django', 'REST Framework', 'SQL / SQLite'],
            'Frontend Development': ['JavaScript (ES6+)', 'React', 'Bootstrap 5', 'HTML5 / CSS3'],
            'Tools & DevOps': ['Git & GitHub', 'Virtual Environments (venv/uv)', 'VS Code', 'MVT Architecture'],
            'Exploratory & Systems': ['COBOL Data Structure', 'Cybersecurity Defense Fundamentals'],
        }
    }
    return render(request, 'pages/skills.html', context)


def contact(request):
    context = {
        'availability': 'Our team is open for group project collaborations, software engineering internships, and developer roles.',
        'location': 'Nairobi, Kenya',    
    }
    return render(request, 'pages/contact.html', context)
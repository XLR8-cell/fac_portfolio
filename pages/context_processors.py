from datetime import datetime

def global_context(request):
    return {
        'site_name': 'GN.dev',
        'author_name': 'Gilbert Nyamberi',
        'author_title': 'Software Engineer & Full-Stack Developer',
        'github_url': 'https://github.com/XLR8-cell',
        'linkedin_url': 'https://linkedin.com/in/gilbert-nyamberi',
        'contact_email': 'gilbertnyamberi1@gmail.com',
        'current_year': datetime.now().year,
    }
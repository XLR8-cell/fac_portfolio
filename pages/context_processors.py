from datetime import datetime

def global_context(request):
    return {
        'site_name': 'FAC_2_TUAL',
        'author_name': 'FAC_2_TUAL Team',
        'author_title': 'Software Engineering Team',
        'github_url': 'https://github.com/XLR8-cell',
        'linkedin_url': 'https://linkedin.com/in/FAC group 2',
        'contact_email': 'team@fac2tual.dev',
        'current_year': datetime.now().year,
    }
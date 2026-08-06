from django.db import models

# Create your models here.
""" 
1. Create a Project model with fields: name, description, tech_stack, github_url, live_url, is_featured 
2. Create a Skill model with fields: name, category, level (Beginner / Intermediate / Expert) 
3. Make migrations and migrate the database 
4. Add 5 sample projects via the Django shell: python manage.py shell 
5. Update your projects view to query the database and pass the results to the template 
6. Display the projects in projects.html using a {% for project in projects %} loop"""


LEVEL_CHOICES = [
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Expert", "Expert"),
]


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=200)
    github_url = models.URLField()
    live_url = models.URLField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.github_url}"


class Skills(models.Model):
    skill_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="Beginner")

    def __str__(self):
        return f"{self.skill_name} - {self.category} - {self.level}"

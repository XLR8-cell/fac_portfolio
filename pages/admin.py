from django.contrib import admin
from .models import Project, Skills


# Register your models here using @Admin.register decorator.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "tech_stack", "is_featured", "github_url", "live_url")
    list_filter = ("is_featured", "tech_stack")
    search_fields = ("name", "tech_stack")
    list_editable = ("is_featured", "tech_stack")
    fieldsets = (
        (
            "Project details",
            {
                "fields": ("name", "description", "tech_stack"),
            },
        ),
        (
            "access",
            {"fields": ("live_url", "github_url")},
        ),
    )
    list_display_links = ("live_url", "github_url","name")

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display=("skill_name", "category", "level")
    list_filter=("level", "category")
    search_fields= ("skill_name", "category")

admin.site.site_header = "Group 2 Adminstration"
admin.site.site_title = "Group 2 Admin"
admin.site.index_title = "Dashboard"


# --create a superuser to log in--

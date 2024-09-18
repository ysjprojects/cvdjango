from django.contrib import admin

# Register your models here.
from .models import Education, Experience, Skill, Project

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)

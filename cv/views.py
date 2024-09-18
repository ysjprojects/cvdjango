from django.shortcuts import render
from .models import Education, Experience, Skill, Project

def index(request):
    education_list = Education.objects.all().order_by('-start_date')
    experience_list = Experience.objects.all().order_by('-start_date')
    skill_list = Skill.objects.all()
    project_list = Project.objects.all()

    context = {
        'education_list': education_list,
        'experience_list': experience_list,
        'skill_list': skill_list,
        'project_list': project_list,
    }
    return render(request, 'cv/index.html', context)

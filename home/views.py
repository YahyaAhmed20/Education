from django.shortcuts import render
from .models import Skill
from .models import Course

def home(request):
    skills = Skill.objects.all()
    courses = Course.objects.filter(is_active=True)

    return render(request, 'home/home.html', {'skills': skills,'courses': courses})
from django.shortcuts import render
from .models import Course

# Create your views here.
def courses(request):
    # Fetch the job list
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})
from django.shortcuts import render

# Create your views here.
def courses(request):
    # Fetch the job list
    return render(request, 'courses/courses.html')
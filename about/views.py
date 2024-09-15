from django.shortcuts import render

# Create your views here.
def about(request):
    # Fetch the job list

    return render(request, 'about/about.html')
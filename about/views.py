# views.py
from django.shortcuts import render
from .models import TeamMember, AboutUsSection

def about(request):
    # Fetch the job list
    team_members = TeamMember.objects.all()
    about_sections = AboutUsSection.objects.all()   
    return render(request, 'about/about.html', {
        'team_members': team_members,
        'about_sections': about_sections})
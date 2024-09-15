from django.shortcuts import render
from .models import Slide, Course, Testimonial, Skill

def home(request):
    slides = Slide.objects.order_by('order')
    courses = Course.objects.order_by('order')
    testimonials = Testimonial.objects.all()
    skills = Skill.objects.all()

    context = {
        'slides': slides,
        'courses': courses,
        'testimonials': testimonials,
        'skills': skills,
    }
    return render(request, 'home/home.html',context)

# Register your models here.
from django.contrib import admin
from .models import Slide, Course, Testimonial, Skill

admin.site.register(Slide)
admin.site.register(Course)
admin.site.register(Testimonial)
admin.site.register(Skill)

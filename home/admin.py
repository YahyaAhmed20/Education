from django.contrib import admin
from .models import Skill
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


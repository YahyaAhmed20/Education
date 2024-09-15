# admin.py
from django.contrib import admin
from .models import TeamMember, AboutUsSection

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

@admin.register(AboutUsSection)
class AboutUsSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)


from django.contrib import admin
from .models import PortfolioCategory, PortfolioItem

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_added')
    search_fields = ('title', 'description')
    list_filter = ('category',)

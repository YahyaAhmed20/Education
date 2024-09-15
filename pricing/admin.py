
from django.contrib import admin
from .models import PricingPlan, Discount

class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name',)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('plan', 'percentage', 'start_date', 'end_date', 'active')
    list_filter = ('active', 'start_date')
    search_fields = ('plan__name',)

admin.site.register(PricingPlan, PricingPlanAdmin)
admin.site.register(Discount, DiscountAdmin)

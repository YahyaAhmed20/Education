# pricing/views.py
from django.shortcuts import render
from .models import PricingPlan, Discount
from datetime import date
from decimal import Decimal


def pricing(request):
    # Fetch the job list
  
    plans = PricingPlan.objects.all()

    discount_dict = {
        discount.plan.id: discount.apply_discount()
        for discount in Discount.objects.filter(active=True, start_date__lte=date.today(), end_date__gte=date.today())
    }

    # Add discounted price to plans
    for plan in plans:
        if plan.id in discount_dict:
            plan.discounted_price = discount_dict[plan.id]
        else:
            plan.discounted_price = Decimal(plan.price)

    context = {
        'plans': plans,
    }
    return render(request, 'pricing/pricing.html', context)
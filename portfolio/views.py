
# Create your views here.
from django.shortcuts import render

from .models import PortfolioCategory, PortfolioItem

# Create your views here.



def portfolio(request):
    # Fetch the job list
    categories = PortfolioCategory.objects.all()
    items = PortfolioItem.objects.all()
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'portfolio/portfolio.html',context)
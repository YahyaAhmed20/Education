
# Create your views here.
from django.shortcuts import render

# Create your views here.



def portfolio(request):
    # Fetch the job list
  
    return render(request, 'portfolio/portfolio.html')
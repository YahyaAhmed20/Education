from django.db import models



class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

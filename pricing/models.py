from django.db import models
from decimal import Decimal


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=20, default='Year')  # Monthly, Yearly, etc.
    features = models.TextField()  # Store as comma-separated values or use JSONField for better structure
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_features(self):
        return self.features.split(',')

class Discount(models.Model):
    plan = models.ForeignKey(PricingPlan, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField()  # Discount percentage
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.percentage}% off {self.plan.name}"

    def apply_discount(self):
        if self.active:
            # Ensure all calculations are done using Decimal
            original_price = Decimal(self.plan.price)
            discount_percentage = Decimal(self.percentage) / Decimal(100)
            discounted_price = original_price * (Decimal(1) - discount_percentage)
            return discounted_price
        return Decimal(self.plan.price)
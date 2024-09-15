from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name

# models.py
class AboutUsSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us_images/')

    def __str__(self):
        return self.title

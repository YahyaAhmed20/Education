from django.db import models

# Skills Model
class Skill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # Optional font-awesome icon class

    def __str__(self):
        return self.title

# Carousel Model

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

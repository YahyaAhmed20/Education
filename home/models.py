from django.db import models

# Create your models here.

class Slide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='slides/')
    order = models.IntegerField()

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    order = models.IntegerField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'Testimonial by {self.author}'

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # FontAwesome icon class

    def __str__(self):
        return self.name

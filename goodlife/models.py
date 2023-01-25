from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class BookTrainer(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Photo(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')

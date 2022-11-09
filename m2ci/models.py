from django.db import models

# Create your models here.
class message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=5000)
    sujet = models.TextField(max_length=5000)



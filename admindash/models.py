from django.db import models

# Create your models here.
class registeraccount(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    cpass = models.CharField(max_length=20)
    role = models.CharField(max_length=20, blank=True)
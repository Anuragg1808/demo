from django.db import models

class PropertyListing(models.Model):
    location = models.CharField(max_length=255)
    max_budget = models.DecimalField(max_digits=12, decimal_places=2)
    min_budget = models.DecimalField(max_digits=12, decimal_places=2)

class registeraccount(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    cpass = models.CharField(max_length=20)

class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)  # Using CharField for phone number to accommodate different formats
    message = models.TextField(max_length=1000)

class User(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
# Create your models here.

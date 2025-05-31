from django.db import models

# Create your models here.
#Write a Django REST API to serialize a Doctor model with fields like name, specialty, and contact details.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    mobile = models.BigIntegerField()

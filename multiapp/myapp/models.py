from django.db import models

# Create your models here.

class userinfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
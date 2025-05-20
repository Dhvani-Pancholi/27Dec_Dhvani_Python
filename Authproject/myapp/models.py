from django.db import models

# Create your models here.

class userSignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    
    
    def __str__(self):
        return self.firstname
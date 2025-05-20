from django.db import models

# Create your models here.


class Usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    pphoto = models.ImageField(upload_to="ProfilePhoto")
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=128)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()


class Notes(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    cate = models.CharField(max_length=100)
    notefile = models.FileField(upload_to="Notesfiles")
    desc = models.TextField()
    username = models.ForeignKey(Usersignup, on_delete=models.CASCADE)
    notechoice = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Recjectd"),
    ]
    status = models.CharField(max_length=10, choices=notechoice)
    updated_at = models.DateTimeField(blank=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()
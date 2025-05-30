from django import forms
from .models import *


class UsersignupForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = "__all__"
        
class updateForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = ["firstname","lastname","username","password","mobile","pphoto","city","state"]      
        

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "cate", "notefile", "desc"]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "msg"]
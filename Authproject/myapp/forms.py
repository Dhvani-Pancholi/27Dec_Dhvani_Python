from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = '__all__'
        
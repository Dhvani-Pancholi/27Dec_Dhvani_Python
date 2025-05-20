from django import forms
from .models import *

class userinfoForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields ='__all__'
        
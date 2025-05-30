from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = userinfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved successfully")
        else:
            print(forms.errors)
        
    return render(request, 'index.html')
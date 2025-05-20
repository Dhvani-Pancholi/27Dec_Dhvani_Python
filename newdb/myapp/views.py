from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

# For insering

def index(request):
    msg =""
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            print("record inserted.")
            msg = "record inserted."
            # return redirect('/')
        else:
            print(form.errors)
            msg = "Error"
        
    return render(request, 'index.html', {'msg': msg})

#for fetch the data
def showdata(request):
    data = userinfo.objects.all()
    return render(request, 'showdata.html', {'data': data})

#For delete the data
def delete(request, id):
    stid = userinfo.objects.get(id=id)
    stid.delete()
    return redirect('/showdata')

#For updating the data
def update(request,id):
    msg =""
    stid = userinfo.objects.get(id=id)
    if request.method == 'POST':
        form = updateForm(request.POST, instance=stid)
        if form.is_valid():
            form.save()
            print("record updated.")
            msg = "record updated."
            return redirect('/showdata')
        else:
            print(form.errors)
            msg = "Error"
    
    return render(request, 'update.html', {'stid': stid})
from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *
# Create your views here.

def admin_home(request):
    data = userinfo.objects.all()
    return render(request, 'admin_home.html', {'data': data})

def admin_delete(request, id):
    data = userinfo.objects.get(id=id)
    data.delete()
    return render(request, 'admin_home.html', {'data': data})

def update(request, id):
    data = userinfo.objects.get(id=id)
    print("ID:", data)
    if request.method == "POST":
        form = userinfoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            print("Record updated!")
            return redirect("showdata")
        else:
            print(form.errors)
    return render(request, "update.html", {"data": data})
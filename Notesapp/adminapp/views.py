from django.shortcuts import render,redirect,get_object_or_404
from noteapp.models import *
from datetime import datetime
from django.core.mail import send_mail
from finalproj import settings

# Create your views here.



def admin_index(request):
    if request.method == "POST":
        username = "admin"
        password = "admin@123"

        unm = request.POST["username"]
        pas = request.POST["password"]

        if username == unm and password == pas:
            print("Login Successfully!")
            return redirect("admin_home")
        else:
            print("Error!Login faild...")
    return render(request, "admin_index.html")


def admin_home(request):
    return render(request, "admin_home.html")


def admin_userinfo(request):
    userdata = Usersignup.objects.all()
    return render(request, "admin_userinfo.html", {"userdata": userdata})


def admin_notesinfo(request):
    notesdata = Notes.objects.all()
    return render(request, "admin_notesinfo.html", {"notesdata": notesdata})

def notes_approved(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.status = "approved"
    notes.updated_at = datetime.now()
    notes.save()
    print("Notes Approved")
    send_mail(
                    subject="Your Notes Approval",
                    message=f"Dear {notes.username.username} !\n\nYour Notes has been approved!\n\nThanks & Regards!\nNotesApp\nTOPS Technologies\n9409937584 | dhvanipancholi7@gmail.com",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[notes.username.username],
                )
    return redirect("admin_notesinfo")


def notes_rejected(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.status = "rejected"
    notes.updated_at = datetime.now()
    notes.save()
    print("Notes rejected")
    send_mail(
                    subject="Your Notes Rejection",
                    message=f"Dear {notes.username.username} !\n\nYour Notes has been rejected!\n\nThanks & Regards!\nNotesApp\nTOPS Technologies\n9409937584 | dhvanipancholi7@gmail.com",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[notes.username.username],
                )
    
    return redirect("admin_notesinfo")
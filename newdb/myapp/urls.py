from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index),
    path("showdata/",views.showdata ,name="showdata"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
    
]

from django.contrib import admin
from django.urls import path, include
from todoapp import views

urlpatterns = [
   path('getalldata/',views.getalldata, name='getalldata'),
   path("gettid/<int:id>/", views.gettid, name='gettid'),
   path("deletetid/<int:id>/", views.deletetid, name='deletetid'),
   path("savedata/", views.savedata, name='savedata'),
   path("updatedata/<int:id>/", views.updatedata, name='updatedata'),
    
]


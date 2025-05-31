from django.contrib import admin
from django.urls import path, include
from apiapp import views

urlpatterns = [
   path('getalldata/',views.getalldata, name='getalldata'),
   path('savedata/', views.savedata, name='savedata'),
   path('getdrid/<int:id>/', views.getdrid, name='getdrid'),
   path('deletedrid/<int:id>/', views.deletedrid, name='deletedrid'),
   path('updatedata/<int:id>/', views.updatedata, name='updatedata'),
    
]
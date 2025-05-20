from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
   path('',views.admin_home,name='admin_home'),
   path('admin_home/<int:id>/',views.admin_delete,name='delete'),
   path('update/<int:id>/',views.update,name='update'),
]
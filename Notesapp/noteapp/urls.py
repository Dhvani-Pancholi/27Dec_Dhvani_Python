from django.contrib import admin
from django.urls import path,include
from noteapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('notes/',views.notes,name='notes'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('userlogout/',views.userlogout,name='userlogout'),
    
] 


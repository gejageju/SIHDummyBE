from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home),
    path('add',views.CreateUserview.as_view()),
    path('view',views.UserView.as_view())
   

]

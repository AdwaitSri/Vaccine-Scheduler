from django.contrib import admin
from django.urls import path
from calc import views

app_name='calc'
urlpatterns=[
         path('',views.index,name='index'),
         path('user_details/', views.user_details, name = "user_details"),
         path('sign-up-page/',views.signup,name='sign-up-page'),


]

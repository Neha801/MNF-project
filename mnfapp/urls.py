from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members-home', views.base, name='base'),
    path('script', views.script_saver, name='script'),
    #path('<int:pk>/upload/', views.upload, name='upload'),
    path('my_scripts', views.my_scripts, name="my_scripts"),
    path('mynarration', views.mynarration, name="mynarration"),
    path('empty', views.empty, name="empty"),
    path('newempty', views.newempty, name="newempty"),



]

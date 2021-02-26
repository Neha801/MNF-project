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

    path('name', views.name, name="name"),
    path('live', views.live, name="live"),
    path('do', views.do, name="do"),
    path('referred', views.referred, name="referred"),
    path('boundaryless', views.boundaryless, name="boundaryless"),
    path('basket', views.basket, name="basket"),
    path('showvideo', views.showvideo, name="showvideo"),
    path('special', views.special, name="special"),
    path('concern', views.concern, name="concern"),
    

]

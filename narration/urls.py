from django.urls import path
from . import views

urlpatterns = [
    # path('', views.sampleNarration, name='sample'),
    path('', views.narrations, name='narration'),
    path('narrations', views.sampleNarrations, name='sampleNarrations'),
    path('mynarrations', views.mynarrations, name='mynarrations'),

]

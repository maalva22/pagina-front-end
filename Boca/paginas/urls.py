from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('contest/', views.contest, name='contest'),
     path('new_contest/', views.new_contest, name='new_contest'),
     path('option/', views.option, name='option'),

]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('creator_homepage/', views.creator_homepage, name='creator_homepage'),
    path('buyer_homepage/', views.buyer_homepage, name='buyer_homepage'),
]

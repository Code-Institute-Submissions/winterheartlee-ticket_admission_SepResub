from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all_events/', views.all_events, name='all_events'),
    path('my_events/', views.my_events, name='my_events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('my_<int:event_id>/', views.my_event_detail, name='my_event_detail'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]

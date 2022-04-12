from django.contrib import admin
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Event, EventAdmin)

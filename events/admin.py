from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Event, EventAdmin)

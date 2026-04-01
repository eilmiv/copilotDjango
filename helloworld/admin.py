from django.contrib import admin
from .models import World


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    list_display = ['name', 'hello_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']

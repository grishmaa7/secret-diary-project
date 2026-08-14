from django.contrib import admin
from .models import Entry, Reflection


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'mood', 'is_private', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['mood', 'is_private', 'created_at']


@admin.register(Reflection)
class ReflectionAdmin(admin.ModelAdmin):
    list_display = ['entry', 'created_at', 'updated_at']
    search_fields = ['entry__title', 'content']
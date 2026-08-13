from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'mood', 'is_private', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['mood', 'is_private', 'created_at']
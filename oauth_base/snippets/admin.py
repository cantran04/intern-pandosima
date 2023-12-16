# snippets/admin.py
from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created')
    list_filter = ('language', 'style', 'owner', 'created')
    search_fields = ('title', 'code', 'owner__username')
    date_hierarchy = 'created'
    ordering = ('created',)

admin.site.register(Snippet, SnippetAdmin)

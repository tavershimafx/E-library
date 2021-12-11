from django.contrib import admin

# Register your models here.
from . models import Holdings


@admin.register(Holdings)
class HoldingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'uploader', 'category', 'uploaded')
    list_filter = ('category', 'uploader', 'uploaded')
    search_fields = ('title', 'authors', 'category', 'uploader', 'uploaded')
    ordering = ('category', 'uploader')


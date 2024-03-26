from django.contrib import admin

from .models import TxtFile, TxtFileInfo


@admin.register(TxtFile)
class TxtFileAdmin(admin.ModelAdmin):
    list_display = ['owner', 'id', 'created_at']


@admin.register(TxtFileInfo)
class TxtFileInfoAdmin(admin.ModelAdmin):
    list_display = ['txt_file']
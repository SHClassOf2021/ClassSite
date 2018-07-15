from django.contrib import admin

# Register your models here.

from .models import Announcement_Title, Announcement_Body

admin.site.register(Announcement_Title)
admin.site.register(Announcement_Body)

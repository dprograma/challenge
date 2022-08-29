from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import DemoNewsModel

class DemoNewsModelAdmin(admin.ModelAdmin):
    list_display = ('demonews', 'created_at') #these are the features to be listed
    list_display_links = ('demonews', 'created_at') #these are the features links

admin.site.register(DemoNewsModel, DemoNewsModelAdmin)
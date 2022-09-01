from django.contrib import admin
from .models import DemoNewsModel

# Register your models here.

class DemoNewsModelAdmin(admin.ModelAdmin):
    list_display = ('newsid', 'name', 'relatedids', 'score', 'title', 'newstype', 'descendants', 'text', 'url', 'created_at') #these are the features to be listed
    list_display_links = ('newsid', 'name', 'relatedids', 'score', 'title', 'newstype', 'descendants', 'text', 'url', 'created_at') #these are the features links

admin.site.register(DemoNewsModel, DemoNewsModelAdmin)
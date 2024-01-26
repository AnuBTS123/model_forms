from django.contrib import admin
from app.models import *
# Register your models here.

class CustomizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['url']
    list_editable=['name']
    search_fields=['name']
    list_filter=['name']
    list_per_page=2

admin.site.register(Topic)

admin.site.register(Webpage,CustomizeWebpage)

admin.site.register(AccessRecord)
from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.PostsModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'date_created']
    list_filter = ['date_created']
    search_fields = ['pk']

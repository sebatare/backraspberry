from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at')
    list_filter = ('created_at',)

admin.site.register(Project, ProjectAdmin)
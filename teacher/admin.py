from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Subject)
class SuvjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','phone','subject']
    search_fields = ['name','phone','subject']
    list_filter = ['subject']
    list_per_page = 10
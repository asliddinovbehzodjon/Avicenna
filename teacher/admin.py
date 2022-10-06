from django.contrib import admin
from .models import BlokTestlar,FanTest
from import_export import  resources
from import_export.admin import ImportExportModelAdmin
class BlokTestlarResource(resources.ModelResource):
    class Meta:
        model = BlokTestlar

class FanTestResource(resources.ModelResource):
    class Meta:
        model = FanTest

@admin.register(BlokTestlar)
class BlokTestlarAdmin(ImportExportModelAdmin):
    resource_class = BlokTestlarResource
    list_display = ['week_code','fio']
    search_fields = ['week_code','fio']
    list_per_page = 10
@admin.register(FanTest)
class FanTestAdmin(ImportExportModelAdmin):
    resource_class = FanTestResource
    list_display = ['fan_nomi','test_kodi','sana']
    list_filter = ['sana','test_kodi','fan_nomi']
    search_fields = ['fan_nomi','test_kodi','oquvchi']
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
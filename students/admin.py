from django.contrib import admin
from import_export import  resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Parent,Student
class ParentResources(resources.ModelResource):
    class Meta:
        model = Parent
@admin.register(Parent)
class ParentAdmin(ImportExportModelAdmin):
    resource_class = ParentResources
    list_display = ['name','region','phone']
    search_fields = ['name','phone']
    list_filter = ['region']
    list_editable = ['region']
    list_per_page = 10
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['image_show','name','phone','one_id']
    search_fields = ['name','phone','one_id']
    list_editable = ['phone']
    list_per_page = 10
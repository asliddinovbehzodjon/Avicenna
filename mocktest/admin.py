from django.contrib import admin

# Register your models here.
from .models import Test
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['subject','teacher','date']
    list_filter = ['date','subject','teacher']
    list_per_page = 10
    search_fields = ['subject','teacher']
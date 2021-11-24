from django.contrib import admin
from home import models
# Register your models here.

class Student(admin.ModelAdmin):
    fields = ("name","email","phone")
    list_display = ("name","email","phone")
admin.site.register(models.student,Student)
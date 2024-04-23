from django.contrib import admin

# Register your models here.
from app.models import Student

class Student_info(admin.ModelAdmin):
    list_display=['sno','sname','sdob','smarks','sphone','saddr','semail']

admin.site.register(Student,Student_info)
from django.contrib import admin

from .models import Grade, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Grade)

from django.contrib import admin

# Register your models here.

from .models import Student, Professor, Exam, Grade

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Exam)
admin.site.register(Grade)

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)



class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

admin.site.register(SubjectMarks,SubjectMarksAdmin)
admin.site.register(studentCard)


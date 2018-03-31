from django.contrib import admin
from .models import Student, Instructor


class InstructorAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)

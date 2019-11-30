from django.contrib import admin
from .models import Course, Lesson, Assignment, Unit


class CourseAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


class AssignmentAdmin(admin.ModelAdmin):
    pass


class UnitAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Unit, UnitAdmin)

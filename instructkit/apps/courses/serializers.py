from shortuuidfield import ShortUUIDField
from rest_framework import serializers

from accounts.models import Student, Instructor
from .models import Course, Unit, Lesson, Assignment


class BaseModuleSerializerMixin:
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()


class CourseSerializer(serializers.ModelSerializer, BaseModuleSerializerMixin):
    # TODO: Issue #1 - https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields
    id = serializers.UUIDField(required=False)
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),
                                                  many=True)
    instructors = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(),
                                                     many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'duration_type', 'start', 'end',
                  'instructors', 'students')


class UnitSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(),
                                                pk_field=serializers.UUIDField())

    class Meta:
        model = Unit
        fields = ('id', 'title', 'description', 'duration_type', 'start', 'end',
                  'course', 'level')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'duration_type', 'start', 'end',
                  'instructor', 'unit')


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'title', 'description', 'duration_type', 'start', 'end',
                  'lesson', 'category', 'url', 'document', 'is_complete')

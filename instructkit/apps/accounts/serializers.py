from rest_framework import serializers

from .models import Student, Instructor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('uid', 'username', 'email', 'first_name', 'last_name',)


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('uid', 'username', 'email', 'first_name', 'last_name',)

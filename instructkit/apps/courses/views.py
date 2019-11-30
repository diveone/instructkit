from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import (Course, Unit, Lesson, Assignment, CourseSerializer, UnitSerializer,
                          LessonSerializer, AssignmentSerializer)


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class UnitListCreateAPIView(ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AssignmentListCreateAPIView(ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

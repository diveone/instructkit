from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import (Course, Unit, Lesson, Assignment, CourseSerializer, UnitSerializer,
                          LessonSerializer, AssignmentSerializer)


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'uid'


class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'uid'


class UnitListCreateAPIView(ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    lookup_field = 'uid'


class UnitRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    lookup_field = 'uid'


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'uid'


class LessonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    lookup_field = 'uid'


class AssignmentListCreateAPIView(ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = 'uid'


class AssignmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field = 'uid'

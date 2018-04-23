from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Instructor, Student
from .serializers import InstructorSerializer, StudentSerializer


class InstructorListCreateAPIView(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorRetrieveEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    lookup_field = 'uid'


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'uid'

from django.urls import path
from .views import (InstructorListCreateAPIView, InstructorRetrieveEditAPIView,
                    StudentListCreateAPIView, StudentRetrieveEditAPIView)

app_name = 'accounts'

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='students'),
    path('students/<uid>/', StudentRetrieveEditAPIView.as_view(), name='student_detail'),
    path('instructors/', InstructorListCreateAPIView.as_view(), name='instructors'),
    path('instructors/<uid>/', InstructorRetrieveEditAPIView.as_view(), name='instructor_detail'),
]

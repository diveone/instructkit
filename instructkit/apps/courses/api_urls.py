from django.urls import path

from .views import (CourseListCreateAPIView, CourseRetrieveUpdateDestroyView,
                    UnitListCreateAPIView, UnitRetrieveUpdateDestroyView,
                    LessonListCreateAPIView, LessonRetrieveUpdateDestroyView,
                    AssignmentListCreateAPIView, AssignmentRetrieveUpdateDestroyView)

app_name = 'accounts'

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='courses'),
    path('units/', UnitListCreateAPIView.as_view(), name='units'),
    path('lessons/', LessonListCreateAPIView.as_view(), name='lessons'),
    path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignments'),
    path('courses/<uid>/', CourseRetrieveUpdateDestroyView.as_view(), name='course_detail'),
    path('units/<uid>/', UnitRetrieveUpdateDestroyView.as_view(), name='unit_detail'),
    path('lessons/<uid>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson_detail'),
    path('assignments/<uid>/', AssignmentRetrieveUpdateDestroyView.as_view(), name='assignment_detail'),
]

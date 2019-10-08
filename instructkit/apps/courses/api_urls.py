from django.urls import path

from .views import (CourseListCreateAPIView, CourseRetrieveUpdateDestroyView,
                    UnitListCreateAPIView, UnitRetrieveUpdateDestroyView)

app_name = 'accounts'

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='courses'),
    path('units/', UnitListCreateAPIView.as_view(), name='units'),
    path('courses/<uid>/', CourseRetrieveUpdateDestroyView.as_view(), name='course_detail'),
    path('units/<uid>/', UnitRetrieveUpdateDestroyView.as_view(), name='unit_detail'),
]

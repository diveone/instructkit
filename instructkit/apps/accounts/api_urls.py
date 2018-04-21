from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveEditAPIView

app_name = 'accounts'

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='students'),
    path('students/<id>/', StudentRetrieveEditAPIView.as_view(), name='student_detail'),
]

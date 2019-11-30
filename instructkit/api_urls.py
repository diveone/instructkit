from django.urls import path, include

app_name = 'instructkit_api_urls'

urlpatterns = [
    path('u/', include('accounts.api_urls', namespace='users')),
    path('courses/', include('courses.api_urls', namespace='courses')),
]

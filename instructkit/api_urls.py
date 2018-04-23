from django.urls import path, include

app_name = 'instructkit_api_urls'

urlpatterns = [
    path('u/', include('accounts.api_urls', namespace='users')),
]

from django.urls import path, include

urlpatterns = [
    path('', include('db_serializer.urls')),
]

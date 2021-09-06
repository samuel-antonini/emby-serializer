from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('emby_serializer.urls')),
]

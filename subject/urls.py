# home/urls.py
from django.urls import path
from .views import Subject

urlpatterns = [
    path('', Subject.as_view(), name='subject'),
]
# home/urls.py
from django.urls import path
from .views import Membership

urlpatterns = [
    path('', Membership.as_view(), name='membership'),
]
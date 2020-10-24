from django.shortcuts import render
# home/views.py
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'
from django.shortcuts import render
# home/views.py
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'about.html'
from django.shortcuts import render
# membership/views.py
from django.views.generic import TemplateView


class Subject(TemplateView):
    template_name = 'subject.html'

from django.shortcuts import render
# membership/views.py
from django.views.generic import TemplateView


class Membership(TemplateView):
    template_name = 'membership.html'
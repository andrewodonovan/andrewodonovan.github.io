# home/views.py
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'about.html'


class Testimonial(TemplateView):
    template_name = 'testimonial.html'


class Faq(TemplateView):
    template_name = 'faq.html'


class Contact(TemplateView):
    template_name = 'contact.html'

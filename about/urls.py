# home/urls.py
from django.urls import path
from .views import About, Testimonial, Faq, Contact

urlpatterns = [
    path('', About.as_view(), name='about'),
    path('testimonial', Testimonial.as_view(), name='testimonial'),
    path('faq', Faq.as_view(), name='faq'),
    path('contact', Contact.as_view(), name='contact'),
]
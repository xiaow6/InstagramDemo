from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HelloDjango(TemplateView):
    template_name = "test.html"
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'index.html'

class AbautPageView(TemplateView):
    template_name = 'about.html'

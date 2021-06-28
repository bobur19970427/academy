from django.shortcuts import render
from django.views.generic import TemplateView

class UserProfieleView(TemplateView):
    template_name = 'profile/index.html'
    


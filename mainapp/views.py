from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Post
# Create your views here.

from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'index.html'

class AbautPageView(TemplateView):
    template_name = 'about.html'

def NewsPageView(request):
    posts = Post.objects
    return render(request, 'news.html', {'posts': posts})


# class NewsPageView(TemplateView):
#     posts = Post.objects
#     template_name = 'news.html'

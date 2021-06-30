from django.shortcuts import render, get_object_or_404
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

class LoginPageView(TemplateView):
    template_name = 'registration/login.html'

class RegistrationPageView(TemplateView):
    template_name = 'registration.html'

class TanlovlarPageView(TemplateView):
    template_name = 'tanlovlar.html'

def News_viewPageView(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, 'news_view.html', {'post': post})

# class News_viewPageView(TemplateView):
#     template_name = 'news_view.html'


# class NewsPageView(TemplateView):
#     posts = Post.objects
#     template_name = 'news.html'

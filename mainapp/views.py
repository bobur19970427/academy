from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from . models import Post,Tanlov
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

def TanlovlarPageView(request):
    tanlovs = Tanlov.objects
    return render(request, 'tanlovlar.html', {'tanlovs': tanlovs})

def News_viewPageView(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, 'news_view.html', {'post': post})

def Tanlov_viewPageView(request, tanlov_id):
    tanlov = get_object_or_404(Tanlov,pk=tanlov_id)
    return render(request, 'tanlov_view.html', {'tanlov': tanlov})

# class News_viewPageView(TemplateView):
#     template_name = 'news_view.html'


# class NewsPageView(TemplateView):
#     posts = Post.objects
#     template_name = 'news.html'

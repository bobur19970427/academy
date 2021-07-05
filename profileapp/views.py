from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import TemplateView
from accounts.models import CustomUser
from .forms import CustomUserChangeForm

class UserProfieleView(TemplateView):
    template_name = 'profile/index.html'
    
# class UsersTableView(TemplateView):
#     users = User.objects
#     template_name = 'profile/users.html'


# def EditProfieleView(request):
#     user = CustomUser.objects.all()
#     return render(request, 'profile/update.html', { 'user': user })
    
def UsersTableView(request):
    user_list = CustomUser.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'profile/users.html', { 'users': users })

class AzobolishPageView(TemplateView):
    template_name = 'profile/azobolish.html'



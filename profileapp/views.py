from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import TemplateView

class UserProfieleView(TemplateView):
    template_name = 'profile/index.html'
    
# class UsersTableView(TemplateView):
#     users = User.objects
#     template_name = 'profile/users.html'
    
    
def UsersTableView(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'profile/users.html', { 'users': users })

    
    


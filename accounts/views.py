from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import TemplateView
from accounts.models import CustomUser
from .forms import CustomUserChangeForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'


def UpdateProfieleView(request,id):  
    records = CustomUser.objects.get(id=id)
    records.username = request.POST['username']
    records.first_name = request.POST['first_name']
    records.last_name = request.POST['last_name']
    records.email = request.POST['email']
    # file uchun
    img_file = request.FILES['image']
    fs = FileSystemStorage('media/media/avatar/')
    filename = fs.save(img_file.name,img_file )
    uploaded_file_path = fs.path(filename)
    # 
    records.image = uploaded_file_path
    records.save()
    return redirect("/profile") 

def EditProfieleView(request, user_id):
    user = get_object_or_404(CustomUser,pk=user_id)
    return render(request, 'profile/update.html', {'user': user})
from django import forms

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import CustomUser
from django.contrib.auth.models import User

from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('first_name','last_name','age','address','job','image')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model=CustomUser
        fields = ('username','first_name','last_name','job','age','email','password1','password2')
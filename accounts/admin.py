from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','first_name','last_name','age','address','job','image']
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('email', 'first_name', 'last_name',)}),
    # )
    # fieldsets = UserAdmin.fieldsets

admin.site.register(CustomUser,CustomUserAdmin)
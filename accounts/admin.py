from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser,Fakulty,Yunalish

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','email','first_name','last_name','age','address','job','image','fakulty','yunalish','gurux')
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('email', 'first_name', 'last_name',)}),
    # )
    # fieldsets = UserAdmin.fieldsets

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','first_name','last_name','image')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )

    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Fakulty)
admin.site.register(Yunalish)
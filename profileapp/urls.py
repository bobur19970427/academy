from django.urls import path
from .views import UserProfieleView,UsersTableView

urlpatterns = [
    path('profile/', UserProfieleView.as_view(), name='profile'),
    path('users/', UsersTableView, name='users'),
]

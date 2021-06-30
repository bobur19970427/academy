from django.urls import path
from .views import UserProfieleView,UsersTableView,EditProfieleView

urlpatterns = [
    path('profile/', UserProfieleView.as_view(), name='profile'),
    path('edit/', EditProfieleView, name='edit'),
    path('users/', UsersTableView, name='users'),
]

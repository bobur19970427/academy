from django.urls import path

from .views import UserProfieleView,UsersTableView,AzobolishPageView


urlpatterns = [
    path('profile/', UserProfieleView.as_view(), name='profile'),
    path('users/', UsersTableView, name='users'),
    path('azobolish/', AzobolishPageView.as_view(), name='azobolish'),
]

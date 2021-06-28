from django.urls import path
from .views import UserProfieleView

urlpatterns = [
    path('profile/', UserProfieleView.as_view(), name='profile')
]

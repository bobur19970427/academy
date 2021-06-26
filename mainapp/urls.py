from django.urls import path
from .views import HomePageView,AbautPageView,NewsPageView,LoginPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AbautPageView.as_view(), name='about'),
    path('news/', NewsPageView, name='news'),
    path('login/', LoginPageView.as_view(), name='login'),
]

from django.urls import path
from .views import HomePageView,AbautPageView,NewsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AbautPageView.as_view(), name='about'),
    path('news/', NewsPageView, name='news'),
]

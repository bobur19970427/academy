from django.urls import path
from .views import HomePageView,AbautPageView,NewsPageView,LoginPageView,RegistrationPageView,News_viewPageView,TanlovlarPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AbautPageView.as_view(), name='about'),
    path('news/', NewsPageView, name='news'),
    path('tanlovlar/', TanlovlarPageView.as_view(), name='tanlovlar'),
    # path('registration/', RegistrationPageView.as_view(), name='registration'),
    path('<int:post_id>/', News_viewPageView, name='news_view'),
]

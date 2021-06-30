from django.urls import path
from .views import SignUpView
from .views import EditProfieleView,UpdateProfieleView

urlpatterns = [
    path('registration/',SignUpView.as_view(),name='registration'),
    path('edit/<int:user_id>', EditProfieleView, name='edit'),
    path('update/<int:id>', UpdateProfieleView, name='update'),
]
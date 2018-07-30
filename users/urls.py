from django.urls import path, re_path
from . import views
from .views import UserProfileCreate

app_name = 'users'
urlpatterns = [
    path('new-user/', views.signup, name='create-user'),
    path('create-profile/', UserProfileCreate.as_view(), name='create-profile'),
]
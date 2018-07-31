from django.urls import path, re_path
from . import views
from .views import UserProfileCreate, UserProfileDetail

app_name = 'users'
urlpatterns = [
    path('new-user/', views.signup, name='create-user'),
    path('create-profile/', UserProfileCreate.as_view(), name='create-profile'),
    path('user/<int:user_id>/profile-detail/<int:profile_id>', UserProfileDetail.as_view(), name='profile-detail'),
]
from django.urls import path, re_path
from . import views
from .views import UserProfileCreate, UserProfileDetail, UserProfileUpdate

app_name = 'users'
urlpatterns = [
    path('new-user/', views.signup, name='create-user'),
    path('create-profile/', UserProfileCreate.as_view(), name='create-profile'),
    path('user/<int:user_id>/profile-detail/<int:profile_id>', UserProfileDetail.as_view(), name='profile-detail'),
    path('user/<int:user_id>/profile/<int:profile_id>/update', UserProfileUpdate.as_view(), name='update-profile'),
]
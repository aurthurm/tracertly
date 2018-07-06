from django.urls import path, re_path
from . import views

app_name = 'users'
urlpatterns = [
    path('new-user/', views.signup, name='create-user'),
]
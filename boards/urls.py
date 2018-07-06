from django.urls import path, re_path
from .views import BoardList, BoardDetail

app_name = 'boards'
urlpatterns = [
    path('all/', BoardList.as_view(), name='board-list'),
    path('detail/<int:pk>/', BoardDetail.as_view(), name='board-detail'),
]
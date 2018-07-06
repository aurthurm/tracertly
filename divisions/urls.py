from django.urls import path, re_path
from .views import SectionList, SectionDetail, SubSectionDetail

app_name = 'divisions'
urlpatterns = [
    path('sections/', SectionList.as_view(), name='section-list'),
    path('section-detail/<int:pk>/', SectionDetail.as_view(), name='section-detail'),
    path('section-detail/sub/<int:pk>/', SubSectionDetail.as_view(), name='subsection-detail'),
]
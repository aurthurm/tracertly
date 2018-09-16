from django.urls import path, re_path
from divisions.views import (
    SectionList, SectionDetail, SectionCreate, SectionUpdate, SectionDelete,
    TeamList, TeamDetail, TeamCreate, TeamUpdate, TeamDelete
)

app_name = 'divisions'
urlpatterns = [
    path('sections/', SectionList.as_view(), name='section-list'),
    path('section-detail/<int:section_id>/', SectionDetail.as_view(), name='section-detail'),
    path('section/add/', SectionCreate.as_view(), name='section-add'),
    path('section/<int:section_id>/update', SectionUpdate.as_view(), name='section-update'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('team-detail/<int:team_id>/', TeamDetail.as_view(), name='team-detail'),
    path('team/add/', TeamCreate.as_view(), name='team-add'),
    path('team/<int:team_id>/update', TeamUpdate.as_view(), name='team-update'),
]

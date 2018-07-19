from django.urls import path, re_path
from boards.views import *

app_name = 'boards'
urlpatterns = [
    path('all/', BoardList.as_view(), name='board-list'),
    path('board/<int:board_id>/detail', BoardDetail.as_view(), name='board-detail'),
    path('board/add/', BoardCreate.as_view(), name='board-add'),
    path('board/<int:board_id>/update/', BoardUpdate.as_view(), name='board-update'),
    path('board/<int:board_id>/delete/', BoardDelete.as_view(), name='board-delete'),
    path('board/<int:board_id>/listing/<int:listing_id>/detail', ListingDetail.as_view(), name='listing-detail'),
    path('board/<int:board_id>/listing/add/', ListingCreate.as_view(), name='listing-add'),
    path('board/<int:board_id>/listing/<int:listing_id>/update/', ListingUpdate.as_view(), name='listing-update'),
    path('board/<int:board_id>/listing/<int:listing_id>/delete/', ListingDelete.as_view(), name='listing-delete'),
    path('board/<int:board_id>/listing/<int:listing_id>/item/add', ItemCreate.as_view(), name='item-add'),
    path('board/<int:board_id>/listing/<int:listing_id>/item/<int:item_id>/detail', ItemDetail.as_view(), name='item-detail'),
    path('board/<int:board_id>/listing/<int:listing_id>/item/<int:item_id>/update', ItemUpdate.as_view(), name='item-update'),
    path('board/listing/item/<int:item_id>/milestone/add', MilestoneCreate.as_view(), name='milestone-add'),
    path('board/listing/item/<int:item_id>/milestone/<int:milestone_id>/update', MilestoneUpdate.as_view(), name='milestone-update')
]
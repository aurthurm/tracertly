from django.contrib import admin
from .models import *

class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'item','status')

admin.site.register(Milestone, MilestoneAdmin)

class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','creator' ,'created')

admin.site.register(Board, BoardAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'board','creator' ,'created')

admin.site.register(Listing, ListingAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'Listing','creator' ,'created')

admin.site.register(Item, ItemAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'item', 'comment_by','comment_date')

admin.site.register(Comment, CommentAdmin)
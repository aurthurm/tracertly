from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Board, Listing, Item

class BoardList(ListView):
	model = Board
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['header'] = "All Boards"
		context['sub_header'] = "A list of all Boards Ever Created in this System"
		return context

class BoardDetail(DetailView):
	model = Board
	context_object_name = 'board_detail'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		board_listings = Listing.objects.all().filter(board=self.get_object()) # name=self.object.name
		all_items = Item.objects.all()
		context['board_listings'] = board_listings
		context['all_items'] = all_items
		return context
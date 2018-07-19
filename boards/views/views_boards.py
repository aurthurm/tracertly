from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import Board, Listing, Item
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
	pk_url_kwarg = 'board_id'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		board_listings = Listing.objects.all().filter(board=self.get_object()) # name=self.object.name
		all_items = Item.objects.all()
		context['board_listings'] = board_listings
		context['all_items'] = all_items
		return context
	
class BoardCreate(LoginRequiredMixin, CreateView):
	model = Board
	fields = ['name', 'description','section', 'subsection', 'public', 'archived']

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class BoardUpdate(UpdateView):
	model = Board
	fields = ['name', 'description','section', 'subsection', 'public', 'archived']

class BoardDelete(DeleteView):
	model = Board
	success_url = "/"

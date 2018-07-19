from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import Board, Listing, Item
from boards.forms import ListingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListingDetail(DetailView):
	model = Listing
	context_object_name = 'listing_detail'
	pk_url_kwarg = 'listing_id'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
class ListingCreate(LoginRequiredMixin, CreateView):
	model = Listing
	fields = ['name', 'description']
	pk_url_kwarg = 'listing_id'

	def get_initial(self):
		board = get_object_or_404(Board, pk=self.kwargs.get('board_id'))
		return {'board':board.pk}

	def form_valid(self, form):
		form.instance.creator = self.request.user
		board = get_object_or_404(Board, pk=self.kwargs.get('board_id'))
		form.instance.board = board
		return super().form_valid(form)

class ListingUpdate(UpdateView):
	model = Listing
	# form_class = ListingForm
	fields = ['name', 'description']
	pk_url_kwarg = 'listing_id'

class ListingDelete(DeleteView):
	model = Listing
	pk_url_kwarg = 'listing_id'
	success_url = "/"

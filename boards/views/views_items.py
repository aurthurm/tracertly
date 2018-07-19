from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ItemDetail(DetailView):
	model = Item
	context_object_name = 'item_detail'
	pk_url_kwarg = 'item_id'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		item = get_object_or_404(Item, pk=self.kwargs.get('item_id'))
		milestones = item.milestone_set.all()
		context['header'] = "All Boards"
		context['milestones'] = milestones
		return context

class ItemCreate(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['name', 'description']
	pk_url_kwarg = 'item_id'

	def form_valid(self, form):
		form.instance.creator = self.request.user
		listing = get_object_or_404(Listing, pk=self.kwargs.get('listing_id'))
		form.instance.Listing = listing
		return super().form_valid(form)

class ItemUpdate(UpdateView):
	model = Item
	fields = ['name', 'description']
	pk_url_kwarg = 'item_id'

class ItemDelete(DeleteView):
	model = Item
	pk_url_kwarg = 'item_id'
	success_url = "/"

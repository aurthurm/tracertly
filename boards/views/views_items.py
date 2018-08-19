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
		assignee = None
		assigned = None
		full_name = None
		if item.assignee:
			if item.assignee.first_name and item.assignee.last_name:
				firstname = item.assignee.first_name[:1]
				lastname = item.assignee.last_name[:1]
				full_name = item.assignee.first_name.capitalize() + " " + item.assignee.last_name.capitalize()
				initials = firstname + lastname
				assignee = initials.upper()
				assigned = "initialz"
			else:
				assignee = "@" + str(item.assignee)
				assigned = "usernem"
		comments = item.item_comments.all()
		milestones = item.milestone_set.all()
		context['header'] = "All Boards"
		context['assignee'] = assignee
		context['full_name'] = full_name
		context['assigned'] = assigned
		context['milestones'] = milestones
		context['comments'] = comments
		commentCreateURL = "board/listing/item/" + str(item.pk) + "/comment/add"
		context['commentCreateURL'] = commentCreateURL
		return context

class ItemCreate(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['name', 'description']
	pk_url_kwarg = 'item_id'
	template_name = 'create-form.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formTitle'] = "Add Item"
		return context

	def form_valid(self, form):
		form.instance.creator = self.request.user
		listing = get_object_or_404(Listing, pk=self.kwargs.get('listing_id'))
		form.instance.Listing = listing
		return super().form_valid(form)

class ItemUpdate(UpdateView):
	model = Item
	fields = ['name', 'description', 'assignee']
	pk_url_kwarg = 'item_id'
	template_name = 'create-form.html'

class ItemDelete(DeleteView):
	model = Item
	pk_url_kwarg = 'item_id'
	success_url = "/"

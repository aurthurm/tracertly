from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MilestoneCreate(LoginRequiredMixin, CreateView):
	model = Milestone
	fields = ['title', 'status']
	pk_url_kwarg = 'milestone_id'

	def form_valid(self, form):
		form.instance.creator = self.request.user
		item = get_object_or_404(Item, pk=self.kwargs.get('item_id'))
		form.instance.item = item
		return super().form_valid(form)

class MilestoneUpdate(UpdateView):
	model = Milestone
	fields = ['title', 'status']
	pk_url_kwarg = 'milestone_id'

class MilestoneDelete(DeleteView):
	model = Milestone
	pk_url_kwarg = 'milestone_id'
	success_url = "/"

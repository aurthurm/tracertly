from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from boards.mixins import AjaxableResponseMixin
from django.http import JsonResponse


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

def milestoneAjaxUpdate(request, milestone_id):
	if request.method == "POST" and request.is_ajax():
		status = request.POST['status']
		milestone = get_object_or_404(Milestone, pk=milestone_id)
		milestone.status = status
		milestone.save()
		data = {
			'message': "Successfully update milestone"
		}
		return JsonResponse(data)
	else:
		return JsonResponse({'status':'Failed'})

class MilestoneDelete(DeleteView):
	model = Milestone
	pk_url_kwarg = 'milestone_id'
	success_url = "/"

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from boards.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from boards.mixins import AjaxableResponseMixin
from django.http import JsonResponse


class CommentCreate(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Comment
    fields = ['comment']
    pk_url_kwarg = 'comment_id'

    # def form_valid(self, form):
    #     form.instance.comment_by = self.request.user
    #     item = get_object_or_404(Item, pk=self.kwargs.get('item_id'))
    #     form.instance.item = item
    #     return super().form_valid(form)
   
    def form_valid(self, form):
        form.instance.comment_by = self.request.user
        item = get_object_or_404(Item, pk=self.kwargs.get('item_id'))
        form.instance.item = item

        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response

class CommentUpdate(UpdateView):
	model = Comment
	# form_class = ListingForm
	fields = ['comment']
	pk_url_kwarg = 'comment_id'

class CommentDelete(DeleteView):
	model = Comment
	pk_url_kwarg = 'comment_id'
	success_url = "/"

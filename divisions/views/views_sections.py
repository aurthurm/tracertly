from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from divisions.models import Section
from boards.models import Board
from django.contrib.auth.mixins import LoginRequiredMixin


class SectionList(LoginRequiredMixin, ListView):
	model = Section

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['header'] = "Sections"
		context['sub_header'] = "Though Divided we work together towards a common goal #specialisation"
		context['colorStyle'] = "section-color"
		return context

class SectionDetail(LoginRequiredMixin, DetailView):
	model = Section
	pk_url_kwarg = 'section_id'
	context_object_name = 'object_detail'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['its_a'] = "Section"
		return context


class SectionCreate(LoginRequiredMixin, CreateView):
	model = Section
	fields = ['name', 'description', 'teams', 'members', 'boards']
	template_name = 'create-form.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formTitle'] = "Add Section"
		return context

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class SectionUpdate(LoginRequiredMixin, UpdateView):
	model = Section
	fields = ['name', 'description', 'teams', 'members', 'boards']
	template_name = 'create-form.html'

class SectionDelete(LoginRequiredMixin, DeleteView):
	model = Section
	pk_url_kwarg = 'section_id'
	template_name = 'confirm-delete.html'
	success_url = "/"

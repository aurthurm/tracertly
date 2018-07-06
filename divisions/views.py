from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Section, SubSection
from boards.models import Board


class SectionList(ListView):
	model = Section
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['header'] = "All Sections."
		context['sub_header'] = "A list of all Sections."
		return context

class SectionDetail(DetailView):
	model = Section
	context_object_name = 'section_detail'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['sub_sections'] = SubSection.objects.filter(mainSection=self.get_object())
		return context

class SubSectionDetail(DetailView):
	model = SubSection
	context_object_name = 'subsection_detail'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
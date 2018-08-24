from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignUpForm
from .models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from boards.mixins import AjaxableResponseMixin
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserProfileDetail(DetailView):
	model = UserProfile
	context_object_name = 'profile'
	pk_url_kwarg = 'profile_id'
	template_name = 'users/profile.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
	
class UserProfileCreate(LoginRequiredMixin, CreateView):
	model = UserProfile
	fields = ['title', 'phone','teams', 'section', 'status', 'about']
	template_name = 'users/create-profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formTitle'] = "Create your Profile"
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class UserProfileUpdate(LoginRequiredMixin, UpdateView):
	model = UserProfile
	fields = ['title', 'phone','teams', 'section', 'status', 'about']
	template_name = 'create-form.html'
	pk_url_kwarg = 'profile_id'

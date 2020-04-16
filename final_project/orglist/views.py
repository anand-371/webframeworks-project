from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from .models import lostfound
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView


def home(request):
	context={
			'posts':lostfound.objects.all()
	}
	return render(request,'orglist/home.html',context)
# Create your views here. 

class PostListView(ListView):
	model=lostfound
	template_name='orglist/home.html'
	context_object_name='posts'
	ordering=['-delivery_date']

class PostDetailView(DetailView):
	model=lostfound

class PostCreateView(LoginRequiredMixin,CreateView):
	model=lostfound
	fields=['item_number','weight','insurance_amount','destination','delivery_date','status','file']
	def form_valid(self, form):
		form.instance.finder = self.request.user
		post = form.save(commit=False)
		post.save()
		return redirect('orglist-home')

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=lostfound
	fields=['item_number','weight','insurance_amount','destination','delivery_date','status','file']

	def form_valid(self, form):
		form.instance.finder = self.request.user
		post = form.save(commit=False)
		post.save()
		return redirect('orglist-home')
	def test_func(self):
		post=self.get_object()
		if self.request.user== post.finder:
			return True
		return False	
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=lostfound
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user== post.finder:
			return True
		return False				

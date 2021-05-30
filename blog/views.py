from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class BlogListView(LoginRequiredMixin,ListView):
	model=Blog
	template_name = 'blog_list.html'

class BlogDetailView(LoginRequiredMixin,DetailView):
	model = Blog
	template_name = 'blog_detail.html'

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Blog
	template_name = 'blog_delete.html'
	success_url = reverse_lazy('blog_list')

	#overriding a function to check if the blog author is the same as the request user (logged in guy )
	def test_func(self):
		obj=self.get_object()
		return obj.author == self.request.user

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Blog
	fields = ('title','body')
	template_name = 'blog_edit.html'

	def test_func(self):
		obj=self.get_object()
		return obj.author == self.request.user

class BlogCreateView(LoginRequiredMixin,CreateView):
	model = Blog
	template_name = 'blog_new.html'
	fields = ('title','body',)

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
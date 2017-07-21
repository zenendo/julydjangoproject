# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):

	model = Post

class PostDetailView(DetailView):

	model = Post

class PostCreateView(CreateView):
	model = Post
	fields = ['title','slug','content','image']

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title','slug','content','image']
	template_name_suffix = '_update_form'

class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('list_posts')
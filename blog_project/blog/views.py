from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import CreatePostForm
from django.urls import reverse_lazy
from .models import Category, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SinglePostView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:create')

    def test_func(self):
        return self.request.user == self.get_object().author


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:create')

    def test_func(self):#required by UserPassesTestMixin for authorization
        return self.request.user == self.get_object().author
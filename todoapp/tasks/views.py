from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Task, Category

from .forms import CreatePostForm

from django.urls import reverse_lazy

# Create your views here.

ACTIVE_STATUSES = ['P', 'IP']

class TasksListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        qs = Task.objects.filter(user=self.request.user)
        f = self.request.GET.get('filter', 'all')
        if f == 'active':
            qs = qs.filter(status__in=ACTIVE_STATUSES)
        elif f == 'completed':
            qs = qs.filter(status='D')
        order = self.request.GET.get('order', 'created_at')
        return qs.order_by(order if order in ('created_at', 'due_date') else 'created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter'] = self.request.GET.get('filter', 'all')
        ctx['order'] = self.request.GET.get('order', 'created_at')
        ctx['tabs'] = [('ALL', 'all'), ('ACTIVE', 'active'), ('COMPLETED', 'completed')]
        return ctx



class SingleTaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

class AddTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreatePostForm
    template_name = 'tasks/add_task.html'
    
    def get_success_url(self):
        return reverse_lazy('tasks:task_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditTaskView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = CreatePostForm
    template_name = 'tasks/edit_task.html'
    
    def get_success_url(self):
        return reverse_lazy('tasks:task_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks:tasks_list')

    def test_func(self):
        return self.request.user == self.get_object().user


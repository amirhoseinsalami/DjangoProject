from django.urls import path
from .views import TasksListView, SingleTaskView, AddTaskView, EditTaskView, DeleteTaskView

app_name = 'tasks'

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
    path('<int:pk>/', SingleTaskView.as_view(), name='task_detail'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('<int:pk>/edit/', EditTaskView.as_view(), name='edit_task'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
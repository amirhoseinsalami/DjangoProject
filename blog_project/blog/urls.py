from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name = 'create'),
    path('<int:pk>/', views.SinglePostView.as_view(), name = 'detail'),
    path('', views.IndexView.as_view(), name = 'posts'),
    path('<int:pk>/edit/', views.EditPostView.as_view(), name = 'edit'),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name = 'delete'),
]
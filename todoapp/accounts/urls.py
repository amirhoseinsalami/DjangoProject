from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView, RegisterView, UpdateProfilePhotoView, UpdateProfileView , CustomLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/edit/', UpdateProfileView.as_view(), name='profile_edit'),
    path('profile/edit/change-photo/', UpdateProfilePhotoView.as_view(), name="change_photo")

]
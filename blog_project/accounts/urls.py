from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required,user_passes_test

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('' , include('django.contrib.auth.urls')),
    path('profile/' , views.profile , name = 'profile'),
    path('register/' , views.register , name = 'register')
]

# accounts/login/ [name='login']
# accounts/register/ [name='register']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
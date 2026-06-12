from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Profile
from .forms import UpdateProfilePhotoForm
from django.shortcuts import redirect

# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        remember = self.request.POST.get("remember_me")
        username = self.request.POST.get("username")

        if remember:
            response.set_cookie("saved_username", username, max_age=60*60*24*30)  # 30 days
        else:
            response.delete_cookie("saved_username")
        return response


class UpdateProfilePhotoView(UpdateView):
    model = Profile
    form_class = UpdateProfilePhotoForm
    template_name = "accounts/change_photo.html"
    success_url = reverse_lazy("accounts:profile_edit")

    def get_object(self):
        return self.request.user.profile

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.POST.get("delete_photo"):
            profile = self.object
            # delete current uploaded file (not the default)
            if profile.photo and profile.photo.name != "profiles/default.png":
                profile.photo.delete(save=False)

            # reset to default image
            profile.photo = "profiles/default.png"
            profile.save()

            return redirect(self.get_success_url())

        return super().post(request, *args, **kwargs)

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)

        remember = self.request.POST.get("remember_me")
        username = self.request.POST.get("username")

        if remember:
            response.set_cookie("saved_username", username, max_age=60*60*24*30)  # 30 days
        else:
            response.delete_cookie("saved_username")

        return response

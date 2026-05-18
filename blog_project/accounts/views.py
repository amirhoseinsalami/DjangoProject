from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.
def profile(request):
    return render(request , 'accounts/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('accounts:profile')
    else:
        form = UserCreationForm()

    return render(request , 'registration/register.html' , { 'form' : form })

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        return super().form_valid(form)

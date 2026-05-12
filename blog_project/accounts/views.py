from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
# Create your views here.
def profile(request):
    return render(request , 'accounts/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('blog:posts')
    else:
        form = UserCreationForm()

    return render(request , 'registration/register.html' , { 'form' : form })


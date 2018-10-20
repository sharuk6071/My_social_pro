from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username','email')
            messages.success(request, f'Account created for {username}!')
            return redirect ('web_app-home')
    else:
        form = UserRegisterForm()
    return render(request,'web_users/register.html',{'form':form})
@login_required
def profile(request):
    return render(request,'web_users/profile.html')

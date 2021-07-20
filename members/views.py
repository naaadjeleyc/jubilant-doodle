from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#from techSupport.members.forms import SignUpForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        
        else:
            messages.success (request,"There was an error logging in. Try again...")
            return redirect('login')
       


    else:
        return render(request,'authenticate/login.html', {})


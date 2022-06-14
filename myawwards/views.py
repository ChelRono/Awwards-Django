from django.shortcuts import render,redirect
from myawwards.models import Post
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

   return render(request, 'index.html')

def post(request):

   posts=Post.objects.all()

   return render(request, 'POST/body.html',{'posts':posts})


def profile(request):
   
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

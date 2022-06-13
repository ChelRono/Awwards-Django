from django.shortcuts import render,redirect
from myawwards.models import Post
from .forms import  UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.

def index(request):

   return render(request, 'index.html')

def post(request):

   posts=Post.objects.all()

   return render(request, 'POST/body.html',{'posts':posts})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

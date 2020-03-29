from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UpdateProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user_profile = Profile(user=new_user)
            user_profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == "POST":
        u_update = UserUpdateForm(request.POST, instance=request.user)
        p_update = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request, f'Account info updated!')
            return redirect('profile')
    else:
        u_update = UserUpdateForm(instance=request.user)
        p_update = UpdateProfileForm(instance=request.user)
    context = {
        'u_update': u_update,
        'p_update': p_update
    }
    return render(request, 'users/profile.html', context)


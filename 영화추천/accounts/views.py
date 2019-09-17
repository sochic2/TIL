from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm

def signup(request):
    
    if request.user.is_authenticated:
        return redirect('page:main')
      
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('page:main')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('page:main')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'page:main')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('page:main')

def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    context = {'people': people,}
    return render(request, 'accounts/people.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user = user_change_form.save()
            return redirect('people', user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    context = {'user_change_form': user_change_form,}
    return render(request, 'accounts/update.html', context)

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('page:main')

@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
    context = {'password_change_form': password_change_form,}
    return render(request, 'accounts/password.html', context)

@login_required
def profile_update(request):
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form,}
    return render(request, 'accounts/profile_update.html', context)

@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)

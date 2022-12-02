from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import conf

from .models import Profile
from .forms import CustomUserCreationForm


def loginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        # username = request.POST.get('username')
        password = request.POST['password']
        # password = request.POST.get('password')

        # IF the username exists authenticate the username and password
        try:
            user = User.objects.get(username=user)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        # IF the user exists login the user
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Username OR Password is incorrect')

        return redirect('profiles')
    return render(request, 'users/login-register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):

    page = 'register'

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(
                request, 'Congratulations, Your Account has been created.')

            login(request, user)
            return redirect('account')

        else:
            messages.error(request, 'error')

    context = {'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)

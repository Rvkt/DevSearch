from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import conf

from .models import Profile


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


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']   # Throwing error
        # username = request.POST.get('username')
        password = request.POST['password']   # Throwing error
        # password = request.POST.get('password')

        # IF the username exists authenticate the username and password
        try:
            user = User.objects.get(username=user)
        except:
            # print('Username does not exists!!!!')
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        # IF the user exists login the user
        if user is not None:
            login(request, user)
        else:
            # print('Username or Password is incorrect')
            messages.error(request, 'Username OR password is incorrect')

        return redirect('profiles')
    return render(request, 'users/login-register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')

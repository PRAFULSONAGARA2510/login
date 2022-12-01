from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from mainapp.forms import NewUserForm


def homeview(request):
    # print(form)
    return render(request, 'homepage.html')


def loginview(request):
    form = AuthenticationForm(request, data=request.POST or None)
    print(form)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("homepage")
    return render(request, 'loginpage.html', context={'form': form})


def registerview(request):
    form = NewUserForm(request.POST or None)
    # print("form valid:",form.is_valid())
    # print('---------------------------------')
    # print(form.errors)
    if form.is_valid():
        user = form.save()
        # login(request, user)
        messages.success(request,"Register Successfully")
        return redirect('loginpage')
    # messages.error(request, "Unsuccessful register, Invalid information..")
    return render(request, 'registerpage.html', context={'form':form})


def logoutview(request):
    logout(request)
    return redirect('homepage')

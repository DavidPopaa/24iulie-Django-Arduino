from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request,user)
            return redirect("accounts:redirect")
        else:
            return HttpResponse("something went wrong...")
    else:
        form = UserCreationForm()
        return render(request, "accounts/signup.html", {"form":form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("accounts:redirect")
        else:
            return HttpResponse("something went wrong...")
    else:
        form = AuthenticationForm()
        return render(request, "accounts/signin.html", {"form":form})


def redirectt(request):
    return render(request, "accounts/redirect.html")
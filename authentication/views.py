from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def signup(rq):
    if rq.method == "POST":
        form = SignupForm(rq.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password']
            cpass = form.cleaned_data['confirm_password']

            if pass1 != cpass:
                messages.error(rq, "Password and confirm password is not matching")

                return render(rq, "authentication/signup.html", {
                    "signupform": form

                })
            else:
                usernamecheck = User.objects.filter(username=username)
                if usernamecheck:
                    messages.error(rq, "Username is already taken")
                    return render(rq, "authentication/signup.html", {
                        "signupform": form
                    })

                user = User.objects.create(
                    username=username,
                    email=email
                )
                user.set_password(pass1)
                user.save()
                messages.success(rq, "Login to continue")
                return redirect("login")



    else:

        form = SignupForm()
        return render(rq, "authentication/signup.html", {
            "signupform": form
        })


def login_page(rq):
    if rq.method == 'POST':
        form = LoginForm(rq.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            userexits = User.objects.filter(username=username).exists()
            if userexits is None:
                messages.error(rq, "User not exist")
                return redirect("signup")
            else:
                user = authenticate(username=username, password=password)
                if user:
                    messages.success(rq, "Logged in successfully")
                    login(rq, user)
                    nexturl = rq.GET.get("next")
                    print("*-" * 100)
                    print(nexturl)
                    if nexturl:
                        return redirect(nexturl)
                        # pass
                    else:
                        return redirect("root")
                else:
                    messages.error(rq, "Incorrect username or password")
                    return render(rq, "authentication/login.html", {
                        "loginform": form
                    })

    form = LoginForm()
    return render(rq, "authentication/login.html", {
        "loginform": form
    })


def logout_page(rq):
    logout(rq)
    messages.success(rq, "Succesfully logout")
    return redirect("signup")

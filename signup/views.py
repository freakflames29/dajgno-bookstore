from django.shortcuts import render
from .forms import SignupForm
# Create your views here.


def signup(rq):
    form = SignupForm()

    if rq.method == "POST":
        form=SignupForm(rq.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(rq, 'signup/welcome.html', {
                "name": form.cleaned_data['user_name']
            })
    
        
    return render(rq, "signup/signup.html",{
        "form":form
    })

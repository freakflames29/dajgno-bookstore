from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=10, label="Your username")
    email = forms.EmailField(label="Your Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Password")

    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, label="Your username")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Password")

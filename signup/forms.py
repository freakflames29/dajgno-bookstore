from django import forms

class SignupForm(forms.Form):
	user_name = forms.CharField(label="Your name",label_suffix=":-",max_length=5,min_length=2)
	age = forms.IntegerField(max_value=80)
	


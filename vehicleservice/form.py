from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "text",
		"placeholder": " username"
	}))

	email = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "email",
		"placeholder": "email-id"
	}))

	password1 = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "password",
		"placeholder": "password"
	}))

	password2 = forms.CharField(widget=forms.TextInput(attrs={
		"class": "input",
		"type": "password",
		"placeholder": "confirm password"
	}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', "password2"]




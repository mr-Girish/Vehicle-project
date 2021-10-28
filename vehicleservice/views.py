from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from .form import *

# Create your views here.
def index(request):
    return render(request,'vehicleservice/index.html')
def about(request):
    return render(request,'vehicleservice/about.html')
def contact(request):
    return render(request,'vehicleservice/contact.html')
def search(request):
    return render(request,'vehicleservice/search.html')
def vehicles(request):
    return HttpResponse('this is mamagement of vehicle')
# def singup(request):
#     return render(request,'vehicleservice/singup.html')
def login(request):
    return render(request,'vehicleservice/login.html')
    


class SinghupView(View):
    def get(self,request):
        fm = SignupForm()
        return render(request,'vehicleservice/singup.html',{'form':fm})

    def post(self,request):
        fm = SignupForm(request.POST)
        # breakpoint()
        if fm.is_valid():
            fm.save()
            messages.success(request, "Singpu successfully !")
            return redirect('singup')
        else:
            return render(request, 'vehicleservice/singup.html', {'form': fm})


class UserLoginForm(View):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))






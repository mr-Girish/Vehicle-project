from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
# from django.contrib.auth import User
# from vehicleservice.models Post
from django.contrib.auth import authenticate,login,logout
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
def navbar(request):
    return render(request,'vehicleservice/navbar.html')
def userpage(request):
    return render(request,'vehicleservice/userpage.html')
    


# class SinghupView(View):
#     def get(self,request):
#         fm = SignupForm()
#         return render(request,'vehicleservice/singup.html',{'form':fm})

#     def post(self,request):
#         fm = SignupForm(request.POST)
#         # breakpoint()
#         if fm.is_valid():
#             fm.save()
#             messages.success(request, "Singpu successfully !")
#             return redirect('singup')
#         else:
#             return render(request, 'vehicleservice/singup.html', {'form': fm})


# class UserLoginForm(View):

#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "text",
#         "placeholder": "enter username"
#     }))

#     password = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "enter password"
#     }))



def handleSignup(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		fname = request.POST['fname']
		lname = request.POST['lname']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		# check for errorneous input

		if len(username)>10:
			messages.error(request, " username must have 10 character")
			return redirect('index')
		if not username.isalnum():
			messages.error(request, "Username should be only the letter or number")
			return redirect('index')
		if password != cpassword:
			messages.error(request, "password and confirm password didn't matched")

		# Create the user
		myuser = User.objects.create_user(username, email, password)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.save()
		messages.success(request, " Your iCoder has been successfully created")
		return redirect('index')


	else:
		return HttpResponse('404 Not found')




def handleLoginn(request):
	if request.method=='POST':
		loginusername=request.POST['loginusername']
		loginpassword=request.POST['loginpassword']

		user = authenticate(username= loginusername,password= loginpassword)

		if user is not None:
			login(request, user)
			messages.success(request,"successfully logged In")
			return redirect('userpage')
		else:
			messages.error(request,"Invalid credentials, please try again")
			return redirect('index')

	return HttpResponse('404 Not found')
	

def handleLogout(request):
	logout(request)
	messages.success(request,"successfully logged out")

	return redirect('index')
	# return HttpResponse('handleLogout')

		# if request.method == 'POST':
		# # get the post parametrs
		# username =render.POST['username']
		# fname =render.POST['fname']
		# lname =render.POST['lname']
		# email =render.POST['email']
		# password =render.POST['password']
		# cpassword =render.POST['cpassword']
    
		# # Create the user
		# myuser= User.objects.create_user(username,email,password)
		# myuser.first_name=fname
		# myuser.last_name=lname
		# myuser.save()
		# messages.success(request,"Your account has been successfully created")
		# return redirect('index')

    
  #   else:









from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request): 
 return render(request, 'home.html')

def signout(request):
  return render(request, "home.html")

def signup(request):
  if request.method == "POST":
   username = request.POST['username']
   email = request.POST['email']
   password = request.POST['password']

   myuser = User.objects.create_user(username, email, password)
   myuser.save()

   messages.success(request, "Your Account has been created successfully.")
   return redirect("signin")
  return render(request, "signup.html")

  

def signin(request):

  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username = username, password=password)
    if user is not None:
      login(request, user)
      return render(request, "home.html",{'username' : username})
    else:
      messages.error(request, "Bad Credentials")
      return redirect("home")
  return render(request, "signin.html")

def signout(request):
  pass




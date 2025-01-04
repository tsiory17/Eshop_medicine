from django.shortcuts import render, redirect
from .models import Product 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def home (request):
  products = Product.objects.all()
  return render(request , 'home.html' , {'products': products})

def about(request):
  return render(request,'about.html',{})

def product (request, pk):
  product = Product.objects.get(id = pk)
  return render (request,'product.html', {'product':product})

def login_customer (request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request , username=username , password = password)
    if user is not None:
      login(request,user)
      messages.success(request,"You are logged in")
     
      return redirect('home')
    else:
      messages.error(request,"Username or Password invalid please try again")
      return render(request,'login.html',{})
  else:
      return render(request,'login.html',{})


def logout_customer (request):
  logout(request)
  messages.success(request, "You have logged out successfully")
  return redirect ('home')

def register_user (request):
  form = SignUpForm()
  if request.method =="POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      
      user = authenticate(username=username , password = password)
      login(request,user)
      messages.success(request,"Registration successful")
      return redirect('home')
    else:
      messages.error(request, "Registration failed , please try again")
      return redirect('register')
  else:
     return render(request,'register.html',{'form' : form})
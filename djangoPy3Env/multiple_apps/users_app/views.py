from django.http import HttpResponse
from django.shortcuts import render

# /users 
def root(request):
    return HttpResponse("placeholder to later display all the list of users")

# /register & /users/new
def register(request):
    return HttpResponse("placeholder for users to create a new user record")

# /login
def login(request):
    return HttpResponse("placeholder for users to log in")

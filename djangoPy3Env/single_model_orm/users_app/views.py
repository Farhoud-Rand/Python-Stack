from django.shortcuts import render, redirect
from . import models

# This function is for render the root route page 
def index(request):
    context = {'users':models.get_all_users()}
    return render(request,"index.html",context)

# This function is used to add new user and redirect to the root route 
def add(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        models.add(first_name,last_name,email,age)
        return redirect ("/")



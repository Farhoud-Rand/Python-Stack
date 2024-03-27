from django.shortcuts import render, redirect
from . import models

# This function is for render the root route page 
def index(request):
    context = {
        'dojos':models.get_all_dojos(), 
        'ninjas':models.get_all_ninjas()
    }
    return render(request,"index.html",context)

# This function is used to add new dojo and redirect to the root route 
def add_dojo(request):
    models.add_dojo(request)
    return redirect ("/")

# This function is used to add new ninja and redirect to the root route 
def add_ninja(request):
    models.add_ninja(request)
    return redirect ("/")
    
# This function is used to delete a dojo and redirect to the root route 
def delete_dojo(request, id):
    models.delete_dojo(id)
    return redirect ("/")
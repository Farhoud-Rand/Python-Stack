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
    if (request.method == 'POST'):
        dojo_name = request.POST['dojo_name']
        dojo_city = request.POST['dojo_city']
        dojo_state = request.POST['dojo_state']
        models.add_dojo(dojo_name,dojo_city,dojo_state)
        return redirect ("/")

# This function is used to add new ninja and redirect to the root route 
def add_ninja(request):
    if (request.method == 'POST'):
        dojo_id = int(request.POST['dojo'])
        ninja_first_name = request.POST['ninja_first_name']
        ninja_last_name = request.POST['ninja_last_name']
        models.add_ninja(dojo_id,ninja_first_name,ninja_last_name)
        return redirect ("/")
    
# This function is used to delete a dojo and redirect to the root route 
def delete_dojo(request, id):
    models.delete_dojo(id)
    return redirect ("/")
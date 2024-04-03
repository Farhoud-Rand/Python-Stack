from django.shortcuts import render, redirect
from . import models

# ******************** C (Create) from CRUD ********************
# Function to display page that allows us to create new show
def create(request):
    return render(request, "new.html")

# Function to add new show to the table
def add(request):
    if request.method == 'POST':
        show_id = str(models.add(request.POST)) 
        return redirect("/shows/"+show_id)

# ******************** R (Read one) from CRUD ********************
# Function to show details of one TV show
def show_details(request, id):
    context = {'show':models.get_info(id)}
    return render(request, "show_info.html", context)

# ******************** R (Read all) from CRUD ********************
# Function to render a page that diplay all shows in show table
def shows(request):
    context = {'shows':models.get_all_shows()}
    return render(request, "shows.html",context)

# ******************** U (Update) from CRUD ********************
# Function to render page that allows us to update show information
def edit(request,id):
    context = {'show':models.get_info(id)}
    return render(request,"edit_show.html", context)

# Function to update show data
def update(request):
    if (request.method == 'POST'):
        show_id = str(models.update(request.POST))
        return redirect("/shows/"+show_id)
    
# ******************** D (Update) from CRUD ********************
def destroy(request, id):
    models.delete(id)
    return redirect("/shows")
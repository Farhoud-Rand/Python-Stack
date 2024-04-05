from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .forms import ShowForm


# ******************** C (Create) from CRUD ********************
# Function to display page that allows us to create new show
def create(request):
    return render(request, "new.html")

# Function to add new show to the table
def add(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something after successful form submission
            show_id = str(models.add(request.POST)) 
            return redirect("/shows/"+show_id)
        else:
            form = ShowForm()
        return render(request, 'new.html', {'form': form})

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
        id = request.POST['id']
        errors = models.Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
        # If the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # Redirect the user back to the form to fix the errors
            return redirect("/shows/"+id+"/edit")
        else:
            # If the errors object is empty, that means there were no errors!
            # Retrieve the show to be updated, make the changes, and save
            show_id = str(models.update(request.POST))
            return redirect("/shows/"+show_id)
    
# ******************** D (Update) from CRUD ********************
def destroy(request, id):
    models.delete(id)
    return redirect("/shows")
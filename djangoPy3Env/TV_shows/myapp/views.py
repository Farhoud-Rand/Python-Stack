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
            instance = form.save()
            # Redirect or do something after successful form submission
            show_id = str(instance.id) 
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
    show = models.get_info(id)
    form = ShowForm(instance=show, initial={'title': show.title, 'network': show.network, 'release_date': show.release_date, 'description': show.description})
    context = {'show':show,'form':form}
    return render(request,"edit_show.html", context)

# Function to update show data
def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        show = models.get_info(id)
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            # Redirect or do something after successful form submission
            return redirect("/shows/"+id)
        else:
            # If form is not valid, render the edit page again with the form and error messages
            context = {'show': show, 'form': form}
            return render(request, "edit_show.html", context)
    # Redirect to the edit page if the request method is not POST
    return redirect("/shows/"+id+"/edit")
  
# ******************** D (Update) from CRUD ********************
def destroy(request, id):
    models.delete(id)
    return redirect("/shows")
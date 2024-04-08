from django.shortcuts import render, redirect
from . import models
from .forms import ProductForm

# Root route will show all elements in product table
def index(request):
    context = {'products':models.get_all}
    return render(request,"index.html", context)

# Function to delete all data in table 
def delete_all(request):
    if request.method == 'POST':
        models.delete()
        return redirect('/')

# HTML Form --> form 1
# **********************
# Function to render the form 1 
def show_form1(request):
    return render(request,'form1.html')

# Function to add new element 
def add1(request):
    if request.method == 'POST':
        errors = models.Product.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # If the errors dictionary contains anything
            # Render the form again to make the user fix errors
            context = {'errors':errors}
            return render(request,"form1.html",context)
        else:
            # If the errors object is empty, that means there were no errors!
            # So we are ready to create new product and add it to table 
            models.add(request.POST) 
            return redirect("/")
        
# Django Form --> form 2
# **********************
# Function to render the form 2 
def show_form2(request):
    form = ProductForm()
    return render(request,'form2.html',{'form': form})

# Function to add new element 
def add2(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process the form data if valid
            # Save the form data to the database
            form.save()
            # Redirect to a success page or display a success message
            return redirect('/')
    else:
    # If there is an error in data we should stay in the form so the method will be get not post
        form = ProductForm()
    return render(request, 'form2.html', {'form': form})

# Django with crispy Form --> form 3
# **********************************
# Function to render the form 3 
def show_form3(request):
    form = ProductForm()
    return render(request,'form3.html',{'form': form})

# Function to add new element 
def add3(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process the form data if valid
            # Save the form data to the database
            form.save()
            # Redirect to a success page or display a success message
            return redirect('/')
    else:
    # If there is an error in data we should stay in the form so the method will be get not post
        form = ProductForm()
    return render(request, 'form3.html', {'form': form})
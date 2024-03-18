from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Root route --> redirect to blogs route
def root(request):
    return redirect ('/blogs')

# Blogs route --> will display the placeholder text
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# New route --> display the string "placeholder to display a new form to create a new blog" 
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# Create route --> redirect to the "/" route 
def create(request):
    return redirect("/")

# /blogs/< number > --> display the string "placeholder to display blog number: {number}"
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# /blogs/< number >/edit --> display the string "placeholder to edit blog {number}" 
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# /blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"
def destroy(request, number):
    return redirect("/blogs")

#  /blogs/json --> return a JsonResponse with title and content keys.
def jsonObject(request):
    context = {
        'title': 'My first blog',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    }
    return JsonResponse(context)
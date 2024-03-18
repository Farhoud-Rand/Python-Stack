from django.http import HttpResponse
from django.shortcuts import render

# /surveys
def root(request):
    return HttpResponse("placeholder to display all the surveys created")

# /surveys/new
def new(request):
    return HttpResponse("placeholder for users to add a new survey")

from django.shortcuts import render, redirect
from .forms import *
from . import models

# Root route will show index page which contains add course form and courses table 
def index(request):
    context = {'form':CourseDescriptionForm(), 'courses':models.get_all_courses()}
    return render(request, "index.html", context)

# Function to add new course from form 
# (add course to course table and description to description table and connect them using 1-1 filed)
def add(request):
    if request.method == 'POST':
        form = CourseDescriptionForm(request.POST)
        if form.is_valid():
            # Create Course instance
            course = models.create_course(form.cleaned_data)
            # Create Description instance associated with the Course
            models.create_description(course,form.cleaned_data)
            return redirect('/')  # Redirect to a success page
    else:
        form = CourseDescriptionForm()
    context = {'form':form, 'courses':models.get_all_courses()}
    return render(request, "index.html", context)

# Function to render a page that contains all comment for this course
def show_comments(request, id):
    context = {'course':models.get_info(id)}
    return render(request,"course_comments.html", context)

# Function to render a page to add new comment 
def add_comment(request, id):
    course = models.get_info(id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course  # Associate the comment with the specific course
            comment.save()
            return redirect('/courses/'+str(id))  # Redirect to course comments 
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form, 'course': course})

def delete_course(request, id):
    models.delete_course(id)
    return redirect('/')
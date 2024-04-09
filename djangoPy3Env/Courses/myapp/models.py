from django.db import models

# Course class
class Course(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

# Description class, which has a one to one relationship with course table
class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

# Comment class, which has a one to many relationship with course table
class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

# function to return all courses 
def get_all_courses():
    return Course.objects.all()

# Function to create new course object
def create_course(data):
    course = Course.objects.create(name=data['name'])
    return course

# Function to create new course description
def create_description(course, data):
    Description.objects.create(course=course, content=data['description'])

# Function to return get course by id and return its information
def get_info(id):
    course = Course.objects.get(id=id)
    return course

# Function to delete course by its ID
def delete_course(id):
    course = get_info(id)
    course.delete()
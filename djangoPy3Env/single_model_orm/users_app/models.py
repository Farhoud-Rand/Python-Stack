from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

# This function is used to return all users information to show them in the table
def get_all_users():
    return User.objects.all()

# This functions is used to add a new user to the User table 
def add(first_name,last_name,email,age):
    User.objects.create(first_name=first_name, last_name=last_name, email_address=email, age=age)

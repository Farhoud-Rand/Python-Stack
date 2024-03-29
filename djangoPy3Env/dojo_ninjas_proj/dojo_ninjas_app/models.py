from django.db import models

# Create the Dojo class model
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default = "old dojo")

# Create the Ninja class model
class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name = 'ninjas', on_delete = models.CASCADE) 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

# This function is used to return all dojos information to show them
def get_all_dojos():
    return Dojo.objects.all()

# This function is used to return all ninjas information to show them
def get_all_ninjas():
    return Ninja.objects.all()

# This functions is used to add a new dojo to the Dojo table 
def add_dojo(request_data):
    dojo_name = request_data['dojo_name']
    dojo_city = request_data['dojo_city']
    dojo_state = request_data['dojo_state']
    Dojo.objects.create(name=dojo_name, city=dojo_city, state=dojo_state)

# This functions is used to add a new ninja to the Ninja table 
def add_ninja(request_data):
    dojo_id = int(request_data['dojo'])
    ninja_first_name = request_data['ninja_first_name']
    ninja_last_name = request_data['ninja_last_name']
    dojo = Dojo.objects.get(id=dojo_id)
    Ninja.objects.create(dojo_id=dojo, first_name=ninja_first_name, last_name=ninja_last_name)

# This functions is used to delete a dojo from the Dojo table 
def delete_dojo(request_data):
    id = request_data["id"]
    dojo = Dojo.objects.get(id = id)
    dojo.delete()
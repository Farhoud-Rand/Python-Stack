from django.db import models
import datetime

# Add Validation 
class ShowManager(models.Manager):
    # Function to check data from form before add it in table
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        # Check title
        if len(postData['title']) < 3:
            errors["title"] = []
            errors["title"].append("Show title should be at least 5 characters")
        if ShowManager.check_if_exists(postData['title']):
            # Before adding new error check if the title in the error dictionary 
            if "title" not in errors:
                errors["title"] = []
                errors["title"].append("This show title is exists! it should be unique")
        # Check Network
        if (postData['network'].isalpha() == False) and len(postData['network']) < 4:
            errors["network"] = "Network name cannot contains numbers or spical characters"
        # Check Release date
        month = datetime.datetime.strptime(postData['release_date'],'%Y-%m-%d').month 
        year = datetime.datetime.strptime(postData['release_date'],'%Y-%m-%d').year
        if month == datetime.datetime.now().month and year == datetime.datetime.now().year :
            errors["release_date"] = "Release date cannot be in the current month and year"
        # Check Description
        if 0 < len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters or empty"

        return errors
    
    # Function to check if the show title is exists or not 
    def check_if_exists(title):
        return Show.objects.filter(title=title).exists()

# Create Show table in database
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 

# ******************** C (Create) from CRUD ********************
# This functions is used to add a new show to the Show table 
def add(request_data):
    title = request_data['title']
    network = request_data['network']
    release_date = request_data['release_date']
    description = request_data['description']
    new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
    return new_show.id

# ******************** R (Read one) from CRUD ********************
# This function will reuturn a show information by its ID
def get_info(id):
    show = Show.objects.get(id=id)
    return show

# ******************** R (Read all) from CRUD ********************
# This function is used to return all shows information to display them 
def get_all_shows():
    return Show.objects.all()

# ******************** U (Update) from CRUD ********************
# Update show data
# **First we need to get new data from form 
#   Note if the user didn't add anything the value will be the old data
# ** Get show entity 
# ** Update values of entity then save 
# ** Return id to go to shows/show_id
def update(request_data):
    id = int(request_data['id'])
    title = request_data['title']
    network = request_data['network']
    release_date = request_data['release_date']
    description = request_data['description']
    show = get_info(id)
    show.title = title
    show.network = network
    show.release_date = release_date
    show.description = description
    show.save()
    return id 

# ******************** D (Update) from CRUD ********************
# This function is used to delete specific show by getting its ID
def delete(id):
    show = get_info(id)
    show.delete()
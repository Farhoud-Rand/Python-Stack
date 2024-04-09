from django.db import models

# Create Show table in database
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

# ******************** R (Read one) from CRUD ********************
# This function will reuturn a show information by its ID
def get_info(id):
    show = Show.objects.get(id=id)
    return show

# ******************** R (Read all) from CRUD ********************
# This function is used to return all shows information to display them 
def get_all_shows():
    return Show.objects.all()

# ******************** D (Update) from CRUD ********************
# This function is used to delete specific show by getting its ID
def delete(id):
    show = get_info(id)
    show.delete()
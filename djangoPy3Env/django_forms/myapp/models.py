from django.db import models

# Add Validation for normal form
class ProductManager(models.Manager):
    # Function to check data from form before add it in table
    def basic_validator(self, postData):
        # add keys and values to errors dictionary for each invalid field
        errors = {}
        # Check Name
        if len(postData['name']) < 4:
            errors["name"] = ("Product name should be at least 4 characters")
        # Check Description
        if 0 < len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters or empty"
        # Check Price
        if int(postData['price']) < 0:
            errors["price"] = "Price should be a positive number"
        # Check Quantity
        if int(postData['quantity']) < 0:
            errors["quantity"] = "Quantity should be a positive number"
        return errors

# Product class
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    objects = ProductManager()

# Function to return all data in table 
def get_all():
    return Product.objects.all()

# Function to delete all data from table 
def delete():
    Product.objects.all().delete()

# Function to add new product 
def add(request_data):
    name = request_data['name']
    description = request_data['description']
    price = request_data['price']
    quantity = request_data['quantity']
    category = request_data['category']
    Product.objects.create(name=name, price=price, quantity=quantity, description=description, category=category)
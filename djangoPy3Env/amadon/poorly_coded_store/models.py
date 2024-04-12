from django.db import models

# Product table
class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Order table
class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Function to return all products
def get_all_product():
    return Product.objects.all()   

# Function to return all orders
def get_all_orders():
    return Order.objects.all() 

# Function to create new product 
def create_order(quantity_from_form,total_charge):
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

# Function to get total charge for all orders 
def get_total_charge():
    total = 0
    # Retrieve all orders from the database
    orders = Order.objects.all()
    # Iterate through each order and sum up the charges
    for order in orders:
        total += order.total_price
    return total

# Function to get a specific product by its id to get its price
def get_product_by_id(id):
    return Product.objects.get(id=id)
    

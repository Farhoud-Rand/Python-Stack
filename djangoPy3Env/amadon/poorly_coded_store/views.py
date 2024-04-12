from django.shortcuts import render,redirect
from . import models

# Page to show all products and put an option to order them
def index(request):
    context = {
        "all_products": models.get_all_product()
    }
    return render(request, "store/index.html", context)

# Function to take the order data for form and create a new order object 
def checkout(request):
    id = int(request.POST['product_id'])
    quantity_from_form = int(request.POST["quantity"])
    product = models.get_product_by_id(id)
    price_from_table = product.price
    total_charge = quantity_from_form * price_from_table
    models.create_order(quantity_from_form, total_charge)
    return redirect('/checkout')

# Page to show all orders and total charge for all orders
def show_checkout(request):
    context = {
        'orders' : models.get_all_orders(), 
        'total' : models.get_total_charge(),
    }
    return render(request, "store/checkout.html", context)
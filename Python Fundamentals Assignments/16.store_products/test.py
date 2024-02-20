from store import *
from products import *

# Create a store instance
store = Store("My store")

# Create a few products
product1 = Product("Phone", 500, "Electronics")
product2 = Product("PS5", 550, "Electronics")
product3 = Product("Sushi", 20, "Food")
product4 = Product("Pizza", 15, "Food")

# Add products to the store
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)
store.add_product(product4)

print ("Products in store:") # Print the products in the store
store.print_products()

# Sell a product from the store
print("\n"+"*"*50)
print("Sell a product from the store:")
store.sell_product(1) 

# Apply inflation to the products in the store
print("\n"+"*"*50)
print("Prices after inflation:")
store.inflation(10)    # Increase prices by 10%
store.print_products() # Print the products in the store

# Apply clearance to products in the "Food" category
print("\n"+"*"*50)
print("Prices after clearance of Food category:")
store.set_clearance("Food", 20)  # Reduce prices by 20% for products in the "Food" category
store.print_products()           # Print the products in the store
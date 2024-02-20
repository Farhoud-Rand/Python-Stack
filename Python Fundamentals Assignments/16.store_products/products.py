# Product class that has 3 attributes: a name, a price, and a category.
# All of these should be provided upon creation.

class Product:
    # This variable to keep track of the IDs
    next_id = 1

    def __init__(self, name, price, category):
        self.id = Product.next_id # Assign a unique ID
        Product.next_id += 1      # Increment the ID for the next product
        self.name = name
        self.price = price
        self.category = category

    # This function will updates the product's price.
    # If is_increased is True, the price should increase by the percent_change provided.
    # If False, the price should decrease by the percent_change provided.
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change) / 100
        else:
            self.price -= (self.price * percent_change) / 100

    # This function will print the name of the product, its category, and its price.        
    def print_info(self):
        print(f"\nProduct Name: {self.name}\nproduct ID: {self.id}\nProduct Category: {self.category}\nProduct Price: {self.price}")
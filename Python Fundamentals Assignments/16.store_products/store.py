# Store class that has 2 attributes: a name and a list of products. 
# The name must be provided upon creation.
# But the products list should be empty.

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    # This function takes a product and adds it to the store
    def add_product(self, new_product):
        self.products.append(new_product)

    # sell_product(self, id) - remove the product from the store's list of products given the id  and print its info.
    def sell_product(self, id):
        # self.products[id].print_info()          # Print the product information
        # self.products.remove(self.products[id]) # Remove the product with make id as the index of the product in the list
        for product in self.products:
            if product.id == id:
                product.print_info()          # Print the product information
                self.products.remove(product) # Remove the product according to its id

    # This function increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    # This function updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

    # Additional functions, to make the test easier print products info
    def print_products(self):
        for product in self.products:
            product.print_info()
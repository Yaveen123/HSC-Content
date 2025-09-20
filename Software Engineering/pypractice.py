'''
1. python class
2. init that accepts args:
    plant_name
    price
    stock_quantity
3. method is_in_stock ()
    takes no args
    returns bool if quantity is > zero otherwise False
4. method sell_plant
    takes one arg, quantity_to_sell
    decrease stock_quantity by the amount sold, only if there is enough stock
    returns "Successfully sold 2 plants", or "Error, not enough stock to sell x plants"
5. a __str__ method that reeturns a string with the plant's details. 
'''






class Plant:
    def __init__(self, plant_name, price, stock_quantity):
        self.plant_name = plant_name
        self.price = price
        self.stock_quantity = stock_quantity
    
    def is_in_stock(self):
        return self.stock_quantity > 0
    
    def sell_plant(self, quantity_to_sell):
        if self.stock_quantity >= quantity_to_sell:
            self.stock_quantity -= quantity_to_sell
            return f'Successfully sold {quantity_to_sell} plants.'
        else:
            return f"Error: Not enough stock to sell {quantity_to_sell} plants."

    def __str__(self):
        return f"Plant: {self.plant_name}\nPrice: {self.price}\nStock: {self.stock_quantity}"
        



# ---------------------

# Create a new plant instance
monstera = Plant('Monstera Deliciosa', 49.95, 50)

# Print the plant details using the __str__ method
print(monstera)

# Check if the plant is in stock
print(f"Is the plant in stock? {monstera.is_in_stock()}")

# Sell a quantity that is in stock
print(monstera.sell_plant(5))
print(f"Updated stock: {monstera.stock_quantity}")

# Try to sell a quantity that is not in stock
print(monstera.sell_plant(100))
print(f"Updated stock: {monstera.stock_quantity}")

# Check if the plant is still in stock (after selling all of them)
monstera.sell_plant(45)
print(f"Is the plant in stock? {monstera.is_in_stock()}")
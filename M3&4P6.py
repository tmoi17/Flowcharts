# increase or decrease of the value of the stock entered 

# input the purchase price per share
price_per_share = float(input("Enter the purchase price per share: $"))

# input the current stock price
current_stock_price = float(input("Enter the current stock price: $"))

# input the quantity of stock 
quantity_of_stock = int(input("Enter the quantity of stock: "))

# compute the increase or decrease of the value of stock entered
increase_or_decrease = (current_stock_price - price_per_share) * quantity_of_stock

# Display new value of the stock"
print(f"Value of the stock is ${increase_or_decrease:.2f}")

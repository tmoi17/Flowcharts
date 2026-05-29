# Amount invested

# Prompt user to enter stock ticker symbol
stock_ticker_symbol = input("Enter the stock ticker symbol: ")

# input the number of shares 
shares = float(input("Enter the number of shares: "))

# input the cost per share 
cost_per_share = float(input("Enter the cost per share: $"))

# compute the amount invested
amount_invested = cost_per_share * shares

# Display the result 
print(f"The amount invested for {stock_ticker_symbol} is: ${amount_invested:.2f}")

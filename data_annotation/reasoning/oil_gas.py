"""
A local gas station is selling gas for 3.00 a gallon. An app company is offering 3.00 a gallon.
An app company is offering .20 cashback per gallon if you fill up at this station.
If someone buys 10 gallons of gas, how much with their gas be, after the cashback rewards?
"""
gas_gallon_station = 3
gas_gallon_app = 3

# price per gallon before cashback
price_per_gallon = 3.00

# number of gallons purchased
gallons_purchased = 10

# cashback per gallon
cashback_per_gallon = 0.20

# total price before cashback
total_price = price_per_gallon * gallons_purchased

# calculate cashback amount
cashback_amount = cashback_per_gallon * gallons_purchased

# total price after cashback
total_price_after_cashback = total_price - cashback_amount

# Print the total price after cashback
print(f"The total price after cashback is ${total_price_after_cashback:.2f}")

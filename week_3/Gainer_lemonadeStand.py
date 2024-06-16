"""
Author: Nadia Gainer
Date: 6/16/24
File Name: Gainer_LemonadeStand.py
Description: lemonade stand file
"""

def calculate_cost(lemons_cost,sugar_cost):
 total_cost = lemons_cost + sugar_cost # Calculating the total cost
 return total_cost # Returning the total cost


def calculate_profit(lemons_cost,sugar_cost,selling_price):
 total_cost = calculate_cost(lemons_cost,sugar_cost)
 profit = selling_price - total_cost
 return profit 
total_cost = calculate_cost(5,2)
cost_output = f"cost of lemons: $5.00 + cost of sugar: $2.00 = total cost: ${total_cost}"
profit_output = f"total cost: ${total_cost}, selling price: $10.00, profit:${calculate_profit(5,2,10)}"

print(cost_output)
print(profit_output)

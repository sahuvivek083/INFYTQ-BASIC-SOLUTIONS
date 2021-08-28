"""Write a python function to create and return a new dictionary from the given dictionary(item:price).
Given the following input, create a new dictionary with elements having price more than 200.

prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}

Sample Input	Expected Output
{ 'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}	{'AAPL': 612.78, 'IBM': 205.55}
{ 'MANGO': 150.45,'POMOGRANATE': 250.67, 'BANANA': 20.55,'CHERRY': 500.10,'ORANGE': 200.75}	{'ORANGE': 200.75, 'CHERRY': 500.1, 'POMOGRANATE': 250.67}
"""
def dictionary(price):
    new_dict= {i: prices[i] for i in prices if prices[i] > 200}
    return new_dict

prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(dictionary(prices))
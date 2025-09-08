""" Exercise 1 """
points = 50 
points_gained = 10 
goints_lost = 5
final_score = points + points_gained - goints_lost
print(final_score)

""" Exercise 2 """
recipe_serves = 4
recipe_eggs = 2
cheese_ounces = 4
num_guests = 6 
eggs_needed = (recipe_eggs / recipe_serves) * num_guests
cheese_needed = (cheese_ounces / recipe_serves) * num_guests

print (eggs_needed)
print (cheese_needed)

""" Exercise 3 """
total_budget = 200 
daily_cost = 25 
trip_length = 5 

money_left = total_budget - (daily_cost * trip_length)
print(money_left)   

""" Exercise 4 """ 
def calculate_price(cost, tip):
    total = cost + (cost * tip)
    return total

print(calculate_price(50, 0.15))

""" Exercise 5 """
def calculate_change(price, paid):
    return paid - price 

print(calculate_change(20, 50))
""" Exercise 6 """
def minutes_till_midnight(hours, minute):
    total_minutes = 24 * 60 
    passed_minutes = hours * 60 + minute
    return total_minutes - passed_minutes

print(minutes_till_midnight(22, 30))
""" Exercise 7 """
def apply_discount(price, discount):
    return price - (price * discount)

def apply_tax(price, sales_tax):
    return price + (price * sales_tax) 
def final_price(price, discount, sales_tax):
    price_after_discount= apply_discount(price, discount)
    return apply_tax(price_after_discount, sales_tax)

print(final_price(85,0.15, 0.08))

""" Problem 1 -Movie Tickets """
num_people = 4
ticket_price = 12 
total_cost = num_people * ticket_price
print(total_cost)
"""Problem 2 """
def total_cost(num_bottles):
    return num_bottles * 2.5

print(total_cost(4))

""" Problem 3 -Birthday Countdown"""
def days_until_birthday(today, birthday):
    return birthday - today     

print(days_until_birthday(5, 12))
""" Problem 4 - Allowance """
weeks = 6
money = weeks * 5 
print(money)
""" Problem 5 - Temp Convert """
def to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(to_fahrenheit(0))
print(to_fahrenheit(100))



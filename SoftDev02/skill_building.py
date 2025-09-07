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

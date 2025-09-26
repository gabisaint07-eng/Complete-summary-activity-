import random 
def roll_dice(number_of_sides, quantity):
    return random.randint(1, (number_of_sides * quantity)) 



def fight(number_of_dice, number_of_sides):
   attack = roll_dice(number_of_dice, number_of_sides)
   return attack 

def main():
    print("Testing roll_dice: ")
    print("roll_dice(5, 7): ", roll_dice(5,7))
    fight(7,4)
    fight(6,2)

main()
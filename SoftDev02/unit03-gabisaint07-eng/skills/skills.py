""" Exercise 1 """

def is_speeding(speed,speedLimit):
    speeding=True 
    if speed > speedLimit:
        return speeding
    if speed <= speedLimit:
        speeding=False
        return speeding 
    

""" Exercise 2"""
import random
def steps():
    steps_walked=random.randint(0,20000)
    print(steps_walked)
    step_goal=10000
    return (steps_walked>=step_goal)

"""Exercise 3"""
def miles_per_hour(distance,duration):
    return (distance/(duration/60.0))

    

def main():
    print('Car is speeding: ', is_speeding(9, 10))
    print('Car is speeding: ', is_speeding(15, 10))
    print("Step goal achievd: ",steps())

    

if __name__ == "__main__":
    main()
import skills
import random
from skills import steps
def test_miles_per_hour():
    val = skills.miles_per_hour(10,12)
    print(10/(12/60.0))
    print("skills test: ", val)
    return val

def test_2():
    val=skills.miles_per_hour(20,15)
    print(20/(15/60.0))
    print("skills test 2: ",val)
    return val 

"""Exercise 4 """
def test_is_speeding():
    val=skills.is_speeding(35,41)
    print(35>=41)
    print("Car is speeding: ",val)
    return val

def test_is_speeding_2():
    val=skills.is_speeding(65,41)
    print(65>=41)
    print("Car is speeding: ",val)
    return val

"Exercise 5 (for real this time)"

def test_steps_true():
    random.seed (50)
    assert steps() == True


def test_steps_false():
    random.seed (1)
    assert steps() == False

def test_steps_exact_goal():
    random.seed (999)
    assert steps() == True


def main():
    test_miles_per_hour()
    test_2()
    test_is_speeding()
    test_is_speeding_2()
    test_steps_true()
    test_steps_false()
    test_steps_exact_goal()

if __name__ == "__main__":
    main()
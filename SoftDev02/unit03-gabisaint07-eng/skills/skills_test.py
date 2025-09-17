import skills
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

    


def main():
    test_miles_per_hour()
    test_2()
    test_is_speeding()
    test_is_speeding_2()

if __name__ == "__main__":
    main()
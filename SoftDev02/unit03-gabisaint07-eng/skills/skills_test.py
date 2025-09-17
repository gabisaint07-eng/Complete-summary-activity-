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


def main():
    test_miles_per_hour()
    test_2()

if __name__ == "__main__":
    main()
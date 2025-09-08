def hello_you():
    input_name =input("What's your name? ")
    print("Hello,", " ", input_name,"!",sep="")
    return input_name


# print("abc", end="")
# print("def", end="-")
# print("ghi")




# hello_you()

# def seashells():
#     print("She ", "ells ", "ea", "hell", sep="s", end= "'")
#     print("s down", end="")
#     print(" by the", end=" ")
#     print("sea", "shore", ".",sep="", end= "")
 
# seashells()

def bad_libs():
    adjective1 = input("Enter a adjective: ")
    noun1 = input("Enter Marvel superhero: ")
    noun2 = input("Enter a place: ")
    noun3 = input("Enter villain: ")
    noun4 = input("Enter silly object: ")
    verb1 = input("Enter verb ending in -ing: ")
    exclamation1 = input("Enter an exclamation: ")
    noun5 = input("Enter animal (plural): ")
    noun6 = input("Enter a food:")
    adjective2 = input("Enter another adjective:")


    print("It was a",adjective1,"day in the Marvel Universe.", "Suddenly,",noun1,"appeared in the middle of", noun2, "to face off against the evil", noun3,".",end="")
    print("The villian was holding a ",noun4, "and was",verb1,"menacingly.",end="")
    print("",exclamation1, "shouted the hero, just as an army of",noun5,"arrived to help.")
    print("Together, they defeated the villian and celebrated by eating",noun6,".","In the end, the hero discovered a new ability: the power of",adjective2,".",end="")

bad_libs()


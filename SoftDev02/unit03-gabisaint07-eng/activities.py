import math 
import random

def squared(x):
    return math.pow(x,2)

def cubed(x):
    return math.pow(x,3)

def coin_toss():
    return random.randint(1,2) 

def main():
    #square = squarrd(4)
    #cube = cubed(4)
    #print ("square of 4 = ", square, "cube = ", cube
    #print(coin_toss())
    #print(coin_toss())
    #print(coin_toss())
    #print(coin_toss())
    #print(coin_toss())
    random.seed(100)
    print(random.randint(1,100))
    print(random.randint(50,500))
    print(random.randint(0))

if __name__ == "__main__":
    main()

# given values
#d = True 
#e = False 
#f = True 
#g = False 
# not_d = False
# not_e = True
# d_or_e = True
# d_or_f = False
# e_or_g = False
# d_and_e = False
# d_and_f = True
# d_^_f = False
# d_^_e = True
# not_d_and_f = False
# you can use () in boolean expressions !

#might get a type error if you do something like "1 == 1", cannot compare a string & a numeric value !

# a=5,b=10, c="abc", d="bcd"
# a == b = False 
# a!= b =True
# a == (b - 5) = True
# c == d = False
# a == c = False 
# a < b = True 
# a <= b = True
# a < 5 = False
# a >= 5 = True 
# c < d = False
# c <= d = True
# b < c = TypeError --- equality vs comparing 2 variables

# #declare more assert statements 



import math 
def squared(x):
    return math.pow(x,2)

def cubed(x):
    return x ** 3

def main():
    square = squared(4)
    cube = cubed(4)

    print("Square of 4 =", square, "cube =",cube)

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

#activity 3.4
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



import math
def squared(x):
    return math.pow(x, 2)
def cubed(x): 
    return math.pow(x, 3)
def main(): 
    square = squared(4)
    cube = cubed(4)
    print("Square of 4 =", square, "cube =", cube)

if __name__ == "__main__":
    main()
    
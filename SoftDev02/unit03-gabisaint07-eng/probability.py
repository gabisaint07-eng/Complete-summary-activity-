import math
def n_choose_one(n):
    """
    Function should return the probability of 
    choosing one specific thing out of n change 
    """
    return 1/n

def n_choose_same_m_times(n,m):
    """
    Returns the probability that you could 
    choose n an m number of times in a row
    """
    return (n_choose_one(n))**m

def number_of_draws_for_probability(n,p):
    """
    Return the number of draws needeed to hit a certain probaility
    """
    failure = 1- n_choose_one(n)
    draws = math.log(1-p, failure)
    return math.ceil(draws)

def n_from_probability(p):
    """
    Return the number of items needed to hit a certain probability p
    when drawing one item at a time.
    """
    # Solve for n in 1 - (1 - 1/n) = p => n = 1 / (1 - p)
    if p >= 1.0:
        raise ValueError("Probability must be less than 1.")
    return math.ceil(1 / (1 - p))

def main():
    #print(number_of_draws_for_probability(10,0.5))
    put = input("Enter a draw probability: ")
    put = float(put)
    n = n_from_probability(put)
    draws = number_of_draws_for_probability(n,0.95)
    print("You would need to draw", draws, "time.")
          
if __name__ == "__main__":
    main()

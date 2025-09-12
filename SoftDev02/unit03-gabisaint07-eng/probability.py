import math
def n_choose_one(n):
    """
    Function should return the probability of 
    pulling one object ouyt of n choices
    """
    return 1/n

def n_choose_same_m_times(n,m):
    """
    Returns the probability of pulling one object out of n choices 
    n times in a row

    """
    return n_choose_one(n)**m

def number_of_draws_for_probability(n,p):
    """
    Return the number of draws needed to pull one object 
    out of n choice with a p percentage chance of sucess
    """
    failure = 1- n_choose_one(n)
    draws = math.log(1-p, failure)
    return draws

def main():
    print(number_of_draws_for_probability (10,0,0.5))

if_

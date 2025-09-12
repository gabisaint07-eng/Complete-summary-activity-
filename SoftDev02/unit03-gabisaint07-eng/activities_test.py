import activities 
import random

#test_ makes pytest work!
def test_square_8():
    #setup
    x = 8 
    expected = 64 

    #invoke 
    actual = activities.squared(x)  

    #analyze
    assert actual == expected

def test_squared_negative_8():
    x = -8 
    expected = 64

    #invoke     def test_coin_toss_heads(): 
        #setup
        expected = 2  # This value depends on the seed!
        random.seed(1)
        #invoke
        actual = activities.coin_toss()
        #analyze
        assert actual == expected
    
    def test_coin_toss_tails():
        #setup 
        expected = 2 
        random.seed(5)
        #invoke
        actual = activities.coin_toss()
        #analyze 
        assert expected == actual
    actual = activities.squared(x)

    #analyze
    assert actual == expected

def test_square_0():
    #setup
    x = 0
    expected = 0 
    #invoke
    actual = activities.squared(x)
    #analyze
    assert actual == expected

def test_cubed_8():
    #setup
    x = 8 
    expected = 512 

    #invoke 
    actual = activities.cubed(x)  

    #analyze
    assert actual == expected
# should also havbe other edge cases for cubed as well!

def test_coin_toss_heads(): 
    #setup
    expected = 1
    #invoke
    actual = activities.coin_toss()
    #analyze
    assert actual == expected
    #this test freakin Stinks because it is random! AND NON REPEATABLE!

def test_coin_toss_tails():
    #setup 
    expected = 2 
    random.seed (5)
    #invoke
    actual = activities.coin_toss()
    #analyze 
    assert expected == actual


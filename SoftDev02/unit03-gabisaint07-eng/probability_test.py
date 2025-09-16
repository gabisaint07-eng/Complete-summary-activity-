import probability 

def test_n_choose_one_fifty_two():
    #setup
    x = 52 
    expected = 1/52
    #invoke
    actual = probability.n_choose_one(x)    
    #analyze
    assert actual == expected

def test_flip_coin_heads_five_times():
    #setup
    n = 2
    m = 5 
    expected = (1/2)**5
    #invoke
    actual = probability.choose_same_m_times(n,m)
    #analyze
    assert actual == expected 

    def test_pull_a_five_from_ten_option_at_eithy_percent():
        #setup 
        n =10 
        p = 0.8
        expected = 7 
        #invoke
        result = probability.number_of_draws_for_probability(n, p)
        assert result == expected 
    
    #setup
def test_how_many_objects_for_a_twenty_percent_pull_rate():
    p = 0.2
    expected = 5 
    #invoke 
    actual  = probability.n_from_probability(p)
    #analyze
    assert actual == expected 





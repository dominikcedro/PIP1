"""
@author: Dominik Cedro
"""
#testweekday
def test_weekday():
    ''' This is a test function for "weekday" function.

        Raises: Assertion error if function weekday works incorrectly
        '''
    from list1_dominik9047 import weekday
    result = weekday(4,8,2009)
    assert result == "Tuesday"

def test_segment_lenght():
    ''' This is a test function for "segment_lenght" function.

            Raises: Assertion error if function works incorrectly
            '''
    from list1_dominik9047 import segment_lenght
    result = segment_lenght(1,10,1,8)
    assert result == [1,8]

#no test for function 3, because it has random output

def test_dec2bin():
    ''' This is a test function for "dec2bin" function.

        Raises: Assertion error if function works incorrectly
        '''
    from list1_dominik9047 import dec2bin
    result = dec2bin(-10)
    assert result == "01010"

#test_dna_complement
def test_dna_complement():
    ''' This is a test function for "dna_complement" function.

        Raises: Assertion error if function works incorrectly
        '''
    from list1_dominik9047 import dna_complement
    result = dna_complement("ATC")
    assert result=="TAG"


#start testing functions
test_weekday()
test_segment_lenght()
test_dec2bin()
test_dna_complement()

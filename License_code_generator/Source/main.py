'''
We generate 200 license code and store them into memory,
then show them in the bash. Every license code consist of
six characters.
'''

from random import *
from sql_interface import *

class code_gen( Random ):

    # The license code generator will choices char from legal_code_context
    # and combine it into a code whose length is 6. This procedure repeat
    # 200 times.
    # When create the random.seed( X ), the same number will be generated if you
    # use the same variable X as the input of function.It's recommend to generate
    # a seed before you use class Random.
    def __init__(self):
        
        legal_code_context = 'abcdefghijklmnopqrstuvwxyz1234567890'
        seed = self.seed( version=2 )
        self.storage = {}
        for code_count in range( 200 ):
            tmp = []
            for bit_count in range( 6 ):
                gen_random_number = self.choice( legal_code_context )
                tmp.append( gen_random_number )
            self.storage[ code_count ] = tmp

    # The storage codes in the memory will post in the screen.
    def __output__(self):
        
        for license_code_ID in range( 200 ):
            output = ''.join( self.storage[ license_code_ID ] )
            print( output )
            
    # Function used to operate the license in SQLite database.
    def __storage__(self, dbpath):

        dbconn = SQLiteInterface( dbpath, self.storage )

if __name__ == '__main__':
    new_instance = code_gen()
    #new_instance.__output__()
    new_instance.__storage__( "lisence_key.db" )

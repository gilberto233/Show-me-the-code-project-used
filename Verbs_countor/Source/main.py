'''
Script to statistics the number of  words in selected file.
'''

import fileinput
import re

class char_statistics():

    # Fetch the contend of .txt file in a string with ifilestream.
    def __init__(self, filepath):

        data = []
        self.storage_t = []
        self.count = 0
        file = fileinput.input( filepath )
        for line in file:
            data.append( line )
        self.storage = ''.join( data )

    # Obtain the number of verbs by splitting the string.
    def __statistics_procedure__(self):

        self.storage_t = re.split( ' ', self.storage )
        self.count = len( self.storage_t )
        print( 'We got %s verbs in specify file.' % self.count )

if __name__ == '__main__':
    new_instance = char_statistics( 'yourfile.txt' )
    new_instance.__statistics_procedure__()

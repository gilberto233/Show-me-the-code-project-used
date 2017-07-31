"""
Script being used to check out if the input stream has specify words from filter file.
When these words are found, relative message will show in the screen. After these procedure
the input stream will be hand in to __examinate_and_substitute__() function. The illegal
words will be substituted with '*' characters which got the same length as origin word.
"""

from sys import argv
import re

class words_filter():

    def __init__(self, sample):
        """
        The illegal words will be obtain from the filter file, saving as a tuple.
        After these procedure, the __examination__() function and 
        __examinate_and_substitute__() function will handle the next.
        :param sample: The word under examined.
        """
        self.sample = sample
        self.buffer = []
        filter_list = open( 'word_filter_README.txt', encoding='utf_8' )
        for word in filter_list:
            self.buffer.append( word.strip( '\n' ) )

        if self.__examination__():
            print( 'Freedom.' )
        else:
            print( 'Human Rights.' )

        print( self.__examinate_and_substitute__() )

    def __examinate_and_substitute__(self):
        """
        Find out if the input stream contains the illegal words. If the answer
        is yes, substitute every characters with '*' character. The final result
        will storaged in result string and return to the upper domain.
        :return: result(string)
        """
        result = ''

        for word in self.buffer:
            if word in self.sample:
                result = self.sample.replace( word, len( word ) * '*' )

        return result

    def __examination__(self):
        """
        Check the input stream  and see if the string has the illegal word, when
        find out the first illegal word, the function will exit and return a flag
        to the upper domain which tells the upper domain whether it find out the
        illegal word.
        :return: illegal_package( bool )
        """
        illegal_package = False

        for word in self.buffer:
            if word in self.sample:
                illegal_package = True
                break

        return illegal_package

if __name__ == '__main__':
    instance = words_filter( argv[1] )

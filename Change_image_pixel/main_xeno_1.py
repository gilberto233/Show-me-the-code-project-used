'''
Script will change the input image's pixel into 1136 * 640.
Which fix for iphone5 used.
'''

import os
import re
from PIL import Image
from sys import argv

class trans_handle( Image.Image ):

    # Create a file pointer, let the __convert__() function
    # handle the next.
    def __init__(self, path):

        all_file = os.listdir( path )
        self.path = path
        available_file = []
        self.size = 1136, 640

        for file in all_file:
            if not file.find( '.jpg' ) == -1:
                available_file.append( file )
        for file in available_file:
           self.__convert__( file )

    # Change the pixel of the buffer to 1136 * 640 which fit for
    # iphone5 used. Save the picture. This may lose the origin
    # proportion of the image.
    def __convert__(self, filename):

        buffer = Image.open( self.path + '/' + filename )
        res = buffer.resize( self.size )
        res.save( filename + '.thumbnail', 'JPEG' )
        buffer.close()

if __name__ == '__main__':
    instance = trans_handle( argv[1] )
    

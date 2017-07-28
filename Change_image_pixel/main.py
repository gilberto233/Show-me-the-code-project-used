'''
Script will change the input image's pixel into 1136 * 640.
Which fix for iphone5 used.
'''

from PIL import Image

class trans_handle( Image.Image ):

    # Create a file pointer, let the __convert__() function
    # handle the next.
    def __init__(self, path):

        self.pic = Image.open( path )
        self.__convert__()
        self.pic.close()

    # Change the pixel of the buffer to 1136 * 640 which fit for
    # iphone5 used. Save the picture. This may lose the origin 
    # proportion of the image.
    def __convert__(self):

        size =  1136, 640
        res = self.pic.resize( size )
        res.save( 'result.thumbnail', 'JPEG' )

if __name__ == '__main__':
    instance = trans_handle( yourfilepath )

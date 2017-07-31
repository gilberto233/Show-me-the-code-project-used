"""
The script will generate a PIN used for identify verifying.
The PIN image being storage in jpeg format. We will render the
image via blur filter given by the ImageFilter library.
"""

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageFilter
from random import *
import string

class Identified_code_generator( Image.Image, Random ):

    def __init__(self):
        """
        Allocating a new draw canvas for painting. The canvas created as RGB mode
        and filled with blank color. The position of every character has been preserved.
        After the PIN has been generated, the image will be saved as jpeg file and
        hand in to __blur__() function.
        """
        background = ImageColor.getrgb( 'white' )
        platform = Image.new( 'RGB', ( 200, 64 ), background )
        draw = ImageDraw.Draw( platform )
        self.font = ImageFont.truetype( 'C:/windows/fonts/Arial.ttf', 40 )
        self.seed( version=2 )

        self.code_buf = []
        self.__generate_PIN__()

        for i in range(4):
            random_height = self.choice( range( 0, 16 ) )
            draw.text( ( 10 + i * 50, random_height ), self.code_buf[i], font=self.font, fill=self.__random_color__() )

        platform.save( 'PIN.jpg', 'jpeg' )
        platform.close()
        self.__blur__()

    def __generate_PIN__(self):
        """
        Generate 4 random characters from selected characters. For this example,
        the selected characters will be one of the ascii_uppercase and natural number
        between 0 to 9.
        :return: None
        """

        for i in range(4):
            self.code_buf.append( self.choice( string.ascii_uppercase + string.digits ) )

    def __random_color__(self):
        """
        This function used for obtaining a RGB tuple from a random color of available
        color below. This is used for making the color of PIN code instability.
        :return: RGB tuple.
        """

        available_color = [
            ImageColor.getrgb( 'red' ),
            ImageColor.getrgb( 'blue' ),
            ImageColor.getrgb( 'yellow' ),
            ImageColor.getrgb( 'green' ),
            ImageColor.getrgb( 'orange' )
        ]

        return self.choice( available_color )

    def __blur__(self):
        """
        Before the blur procedure, the image file should be save first, so the
        characters could be handle as part of a image rather than a dependency
        part of canvas.
        Render the picture through ImageFilter, apply GaussianBlur to the 
        PIN code, and save the file.
        :return: None
        """

        platform = Image.open( 'PIN.jpg' )
        draw = platform.filter( ImageFilter.GaussianBlur )
        platform.save( 'PIN.jpg', 'jpeg' )
        platform.close()

if __name__ == '__main__':
    instance = Identified_code_generator().__generate_PIN__()

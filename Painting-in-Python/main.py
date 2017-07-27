'''
Define a class named window open the specify image in the initiative process.
Window class contains function which used to add number 'num' in selected color.

4 arguement you should configuration on your own when you inherit a Frame class:
parent: The Super-Window of the current window,
id: -1 simplify the current window is default. It's about the priority and identifier.
pos: Position of the window. ( Still got no idea what the doc means. )
title: The title of the current window.
'''

import wx

class window( wx.Frame ):

    # Entry of class window. The window will be created and the file path be transferred
    # to self.__add__.
    def __init__(self, filename, num):

        instance = wx.App()
        self.__add__( filename, num )
        instance.MainLoop()

    # Convert the JPEG format file into bitmap so the wxPython could paint it out.
    # Bind the recall function __generate__ with wx.EVT_PAINT behavior so the function would
    # run every time the window being repainted.
    def __add__(self, filename, num):

        icon = wx.Image(filename, wx.BITMAP_TYPE_JPEG)
        self.icon_bit = icon.ConvertToBitmap()
        self.size = self.icon_bit.GetWidth(), self.icon_bit.GetHeight()
        self.font_size = self.icon_bit.GetHeight() / 10
        self.num = num
        wx.Frame.__init__(self, parent = None, id = -1, title = 'image', pos = wx.DefaultPosition, size = self.size)

        self.Bind( wx.EVT_PAINT, self.__generate__ )
        self.Center()
        self.Show( True )

    # Paint the image and text. The panel being draw here.
    # Restrict the initiative scope of the client.
    def __generate__(self, other):

        dc = wx.PaintDC(self)

        dc.DrawBitmap( self.icon_bit, 10, 0, True )

        font = wx.Font(self.font_size, wx.FONTFAMILY_SCRIPT, wx.SLANT, wx.BOLD, True)
        dc.SetFont( font )
        dc.DrawText(self.num, self.font_size * 8, self.font_size )

        self.SetClientSize( self.size )

if __name__ == '__main__':
    #input_stream = raw_input()
    new_instance = window( filename = yourfilename, num = '1' )

"""
Script download the pictures in specify site which only available in 
tieba.baidu.com. What's more, the crawler finishes its work under the
asist of multiprocessor.
"""
from sys import argv
from multiprocessing.dummy import Pool
import urllib.request, re, os

class image_crawler():
    
    def __init__(self, param):
        """
        Recieve three parameters: Website's URL; Storage path in your hardware;
        Number of your device's core.
        param: Input stream
        """
        if ( len( param ) < 3 ):
            print( 'Usage: python crawler.py $URL $dest_folder $num_of_threads' )
            exit()
        self.website_url = param[1]
        self.dest = param[2]
        self.thread = param[3]

        if not os.path.exists( self.dest ):
            os.makedirs( self.dest )
        os.chdir( self.dest )

        self.__agent__()

    def __agent__(self):
        """
        Agent will take care of the remain download task by analysing
        available image URL and hand in to __download_image__() function.
        return: None
        """
        html_buffer = self.__fetch_html__()
        download_list = []

        if html_buffer:
            available_image_url = self.__fetch_image_url__( html_buffer )
            if available_image_url:
                for img in available_image_url:
                    if img not in download_list:
                        download_list.append( img )
                self.__download_image__( download_list )
            else: exit()
        else: exit()

    def __fetch_html__(self):
        """
        Fetch the website's hyper-text. Return the html file in string
        format. Function with timeout consideration.
        return: web_in_html.read()
        """
        print( 'Fetching html.' )

        for i in range(5):
            try:
                web_in_html = urllib.request.urlopen( self.website_url )
                return str( web_in_html.read() )
            except:
                pass
        print( 'Response timeout error.' )
        return None

    def __fetch_image_url__(self, content):
        """
        Obtain available image URL in the html file by regular expression
        analysing.
        return: available_object
        """
        print( 'Fetching image object url.' )
        pattern = '<img pic_type=... class="BDE_Image" src="(.*?)"'

        available_object = re.findall( pattern, content )
        print( '%d images found in this page.' % ( len( available_object ) ) )
        return available_object

    def __download_image__(self, list):
        """
        Bind the __download__() function with multiprocessor API.
        return: None
        """
        print( 'Downloading.' )

        download_info = [ ( single, os.path.basename( single ) ) for single in list ]
        pool = Pool( int( self.thread ) )
        pool.map( self.__download__, download_info )

    def __download__(self, dparam):
        """
        Download the specify image in website and storage them into local
        filesystem. Function with timeout consideration.
        return: None
        """
        ( url, filename ) = dparam

        for i in range(6):
            try:
                with open( filename, 'wb' ) as local_file, urllib.request.urlopen( url, timeout=20 ) as response:
                    data = response.read()
                    local_file.write( data )
                return
            except: pass
        print( 'Download failed: %s' % url )

if __name__ == '__main__':
    instance = image_crawler( argv )

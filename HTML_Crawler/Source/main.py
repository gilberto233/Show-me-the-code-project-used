'''
Script contains measures which crawl information from website.
You can obtain:
Header by __collect_header__()
Body by __collect_phrase__()
Link by __collect_link__()
'''

import re
from sys import argv

class html_collector():

    def __init__(self, mode, filepath):

        self.html_file = open( filepath )
        self.mode = { 'header':1, 'phrase':2, 'link':3 }
        if self.mode[mode] == 1:
            self.__collect_header__()
        elif self.mode[mode] == 2:
            self.__collect_phrase__()
        elif self.mode[mode] == 3:
            self.__collect_link__()
        self.html_file.close()

    def __collect_header__(self):

        for line in self.html_file:
            buffer = re.match( r'<h1>(.*)</h1>', line )
            if buffer:
                print( 'Header:' + buffer.group(1) )

    def __collect_phrase__(self):

        for line in self.html_file:
            buffer = re.match( r'<p.*>(.*)</p>', line )
            if buffer:
                print( 'Phrase:' + buffer.group(1) )

    def __collect_link__(self):

        for line in self.html_file:
            buffer = re.match( r'<p.*><a href=(.*)>(.*)</a>(.*)</p>', line )
            if buffer:
                print( 'Link:' + buffer.group(1) + '\nShow as ' + buffer.group(2) + ' found on ' + buffer.group(3) )

if __name__ == '__main__':
    instance = html_collector( argv[1].strip( '-' ), argv[2] )

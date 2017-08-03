"""
Script finish two process:
1. Obtain data from local text file and storage the data
into excel file.
2. Obtain data from excel file and translate them into
XML format, then storage them into local filesystem as
XML file.
"""
from lxml import etree
import xlwt, re, xlrd

class excel_exchange():

    def __init__(self):
        """
        Entry function. Create a workbook and table in the
        excel file, gain the data from local text file, and
        storage them into excel file.
        Then load the data from selected excel file, create
        the XML element tree with etree library. Then translate
        the data into XML format.
        """
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet( 'sheet1' )

        self.__text_to_excel__()

        self.workbook.save( 'workbook.xls' )

        self.__excel_to_xml__()

    def __excel_to_xml__(self):
        """
        Load the data from excel workbook and storage them
        into local XML file.
        :return: None
        """
        excel_file = xlrd.open_workbook( 'workbook.xls' )
        sheet = excel_file.sheet_by_name( 'sheet1' )

        dict_buffer = {}
        for row in range(3):
            buffer = []
            for col in range( 0, sheet.ncols ):
                buffer.append( sheet.cell( row, col ).value )
            dict_buffer[ row ] = buffer

        tree = etree.ElementTree( etree.Element( 'data' ) )
        tree.getroot().text = '\n\t'
        for tag in dict_buffer:
            new_line = '\n\t\t'
            sub1 = etree.SubElement( tree.getroot(), 'tag', { 'tag': dict_buffer[ tag ][0] } )
            sub1.text = new_line
            metadata1 = etree.SubElement( sub1, 'metadata1', { 'metadata1': dict_buffer[ tag ][1] } )
            metadata2 = etree.SubElement( sub1, 'metadata2' )
            metadata3 = etree.SubElement( sub1, 'metadata3' )
            metadata1.text = dict_buffer[ tag ][1]
            metadata2.text = dict_buffer[ tag ][2]
            metadata3.text = dict_buffer[ tag ][3]
            metadata1.tail = new_line
            metadata2.tail = new_line
            new_line = '\n\t'
            metadata3.tail = new_line
            sub1.tail = '\n'

        tree.write( 'data.xml', encoding='UTF-8', xml_declaration=True )

    def __text_to_excel__(self):
        """
        Load the data from local text file and storage them into
        excel file.
        :return: None
        """
        pattern1 = '"(.*?)":\["(.*?)",(.*?),(.*?),(.*?)\]'
        pattern2 = '"(.*?)" : "(.*?)"'
        pattern3 = '\[(\w+), (.*?), (.*?)\]'

        with open( 'Python_in_Access_README.txt', encoding='utf_8' ) as self.file:
            buffer = ''
            for line in self.file:
                buffer += line.strip( ' \n\t' )
            data = re.findall( pattern1, buffer.strip() )

            for row in range(3):
                for col in range(5):
                    self.worksheet.write( row, col, data[row][col] )

if __name__ == '__main__':
    instance = excel_exchange()

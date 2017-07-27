import sqlite3

class SQLiteInterface():

    # Start a connection to SQLite database, create a new table used to storage
    # license key. Trigger the __exec__() function.
    def __init__(self, filepath, data_set ):

        self.filepath = filepath
        self.data_set = data_set
        conn = sqlite3.connect( filepath )
        self.pointer = conn.cursor()

        self.__exec__()

        conn.commit()
        conn.close()

    # Custom your execution here.
    def __exec__(self):

        self.__add_data__()
        self.__read_data__()

    # Write license key.
    def __add_data__(self):

        try:
            self.pointer.execute("CREATE TABLE licence_key (ID, key)")
            for ID in range( len( self.data_set ) ):
                tmp = [ str(ID), ''.join( self.data_set[ID] ) ]
                self.pointer.execute( "INSERT INTO licence_key VALUES (?,?)", tmp )
        except BaseException:
            #print( 'Exception.' )
            pass

    # Read license key.
    def __read_data__(self):

        for row in self.pointer.execute( 'SELECT * FROM licence_key ORDER BY ID' ):
            print( row[1] )

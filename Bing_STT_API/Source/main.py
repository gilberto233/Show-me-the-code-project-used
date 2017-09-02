"""
The main entry of STT project.
"""
#!/usr/bin/env python
import Record, STT_API

class function_entry():

    def __init__(self):
        self.__start__()

    def __start__(self):
        instance = Record.Record()
        STT_API.STT_API( instance.get_file_name() )

if __name__ == '__main__':
    instance = function_entry()

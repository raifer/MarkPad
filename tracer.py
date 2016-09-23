# -*- coding: utf-8 -*-
"""Tracer module contains only one class : Tracer"""

import os
import time

class Tracer(object):
    """Class Tracer(log_file_path)
    Tracer object  writes trace in the log_file_path
    Tracer object is callable, you can print your trace directly. e.g. with my_tracer('My first log')
    Methods h1, h2 and h3 print your log surrounded with # like markdown format"""
    
    def __init__(self, log_path):
        self.log_file = open(log_path, mode = 'w', buffering = 1, encoding = 'utf8')        
    # end def
    
    def __del__(self):
        """Close the file before del object"""
        self.log_file.close()
    # end def
    
    def __call__(self, s):
        """ my_tracer(s) --> None, write string s in the log file"""
        self.print(s)
    # end def
    
    def print(self, s):
        """print(s) --> None, write string s in log file"""
        self.log_file.write(s + '\n')
    # end def
    
    def h1(self, s):
        """h1(s) --> None,
        write string s surrounded by one "#".
        This is a level 1 header in markdown language""" 
        self.print('# ' + s + ' #')
    # end def
    
    def h2(self, s):
        """h2(s) --> None,
        write string s surrounded by two "#".
        This is the second level header in markdown language""" 
        self.print('## ' + s + ' ##')
    # end def
    
    def h3(self, s):
        """h3(s) --> None,
        write string s surrounded by three "#".
        This is the third level header in markdown language""" 
        self.print('### ' + s + ' ###')
    # end def
    
    def print_time(self):
        """print_time() --> None, print time in log file"""
        self.print(time.strftime("%A %d %B %Y %H:%M:%S"))
    # end def
# end class log
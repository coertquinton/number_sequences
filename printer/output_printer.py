'''
Created on 18 Jan 2017

@author: Quinton
'''

from printer.simple_number_printer import SimpleNumberPrinter
from printer.vertical_dots_printer import VerticalDotsPrinter

#==============================================================================
class OutputPrinter(object):
    
    SIMPLE_NUMBERS = 1
    VERTICAL_DOTS = 2
    
    _printer_types = {
        SIMPLE_NUMBERS: 'Print a simple list of numbers to indicate sequences',
        VERTICAL_DOTS: 'Print a list of vertical dots to represent each number',
    }
    
    #--------------------------------------------------------------------------
    def select_printer(self, printer_type=SIMPLE_NUMBERS):
        if printer_type == self.SIMPLE_NUMBERS:
            return SimpleNumberPrinter()
        
        if printer_type == self.VERTICAL_DOTS:
            return VerticalDotsPrinter()  
            
    #--------------------------------------------------------------------------
    def validate_printer(self, printer_type):
        if self._printer_types.has_key(printer_type):
            return True
            
        return False
            
    #--------------------------------------------------------------------------
    def display_printer_options(self):
        print 'Please select a printer by typing the corresponding number'
        for key, value in self._printer_types.items():
            print str(key) + ' : ' + value 

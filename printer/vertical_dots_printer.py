'''
Created on 18 Jan 2017

@author: Quinton
'''

#==============================================================================
class VerticalDotsPrinter:
    
    #--------------------------------------------------------------------------
    def print_output(self, number_sequence):
        
        printer_output = self.create_printer_output(number_sequence)
        
        for line in printer_output:
            print line
    
    #--------------------------------------------------------------------------
    def create_printer_output(self, number_sequence):
        
        printer_sequence = []       
        
        for i in range(max(number_sequence), 0, -1):
            line = ''
            
            for number in number_sequence:
                if number >= i:
                    line += ' * '
                else:
                    line += '   '
            #print line        
            printer_sequence.append(line)
        return printer_sequence
            
                    
#------------------------------------------------------------------------------
if __name__ == '__main__':
    print 'Test vertical number printer'

    printer = VerticalDotsPrinter()
    test_sequence = [1, 10, 8, 4, 7, 2, 0, 8, 5]
    printer.print_output(test_sequence)

    print 'Test program terminated'
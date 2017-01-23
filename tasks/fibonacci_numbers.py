'''
Created on 19 Jul 2016

@author: Quinton
'''

from abstract_task import AbstractTask

#==============================================================================
class FibonacciNumbers(AbstractTask):

    #--------------------------------------------------------------------------
    def receive_input(self):
        '''
        Specify and receive each piece of input the class will need from 
        the user to complete the task.
        '''
        print 'Printing Fibonacci numbers selected.'
        print 'Specify how many numbers must be in the Fibonacci sequence: '
        total_numbers = raw_input('Total Fibonacci numbers: ')

        if self.validate_input(total_numbers):
            self._end = int(total_numbers)
            return True
        else:
            return False

    #--------------------------------------------------------------------------
    def validate_input(self, total_numbers):
        '''
        '''
        try:
            if not total_numbers.isdigit():
                print 'Specified number of Fibonacci numbers %s must be a positive number but it is not.' % (total_numbers)
                print 'Generating Fibonacci numbers will abort.'
                return False

            total_numbers = int(total_numbers)
            if total_numbers < 1:
                print 'Must specify a positive total amount of numbers.'
                return False
            
            return True

        except:
            print 'How many Fibonacci numbers %s must be an integer.' % total_numbers
            print 'Generating Fibonacci numbers will abort.'
            return False

    #--------------------------------------------------------------------------
    def process(self):
        '''
        do all tasks needed to get the final result
        '''
        self.generate_fibonacci(self._end)

    #--------------------------------------------------------------------------
    def generate_fibonacci(self, number):

        number_1, number_2 = 0, 1
        for x in range(number):
            self._output.append(number_1)
            number_1, number_2 = number_2, number_1 + number_2

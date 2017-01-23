'''
Created on 19 Jul 2016

@author: Quinton
'''

import math
from abstract_task import AbstractTask

#==============================================================================
class PrimeNumbers(AbstractTask):

    #--------------------------------------------------------------------------
    def receive_input(self):
        '''
        Specify and receive each piece of input the class will need from 
        the user to complete the task.
        '''
        print 'Please enter the following data to start generating prime numbers:'
        start = raw_input('Starting number: ')
        end = raw_input('End number: ')
        
        if self.validate_input(start, end):
            self._start = int(start)
            self._end = int(end)
            return True
        else:
            return False

    #--------------------------------------------------------------------------
    def validate_input(self, start, end):
        '''
        '''
        try:
            if not (start.isdigit() and end.isdigit()):
                print 'Starting number %s and end number %s must both be numbers but they are not.' % (start, end)
                print 'Generating prime numbers will abort.'
                return False
            
            start_number = int(start)
            end_number = int(end)

            if start_number >= end_number:
                print 'The starting number must be smaller than the end number.'
                print 'Generating prime numbers will abort.'
                return False
            
            return True
            
        except:
            print 'Starting number %s and end number %s must both be positive integers but they are not.' % (start, end)
            print 'Generating prime numbers will abort.'
            return False

    #--------------------------------------------------------------------------
    def process(self):
        '''
        do all tasks needed to get the final result
        '''

        for x in range(self._start, self._end + 1):
            if self.confirm_prime(x):
                self._output.append(x)

    #--------------------------------------------------------------------------
    def confirm_prime(self, number):
        '''
        '''
        if number == 1:  #must be greater than one to be a prime
            return False

        if number == 2:
            return True  #always a prime

        square_root = math.sqrt(number)
        end_search = int(math.ceil(square_root)) + 1
        
        for x in range(2, end_search):
            #if any integer divides into the number cleanly it cannot be a prime number.
            if number % x == 0:
                return False
        return True

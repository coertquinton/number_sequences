'''
Created on 19 Jul 2016

@author: Quinton
'''

from abstract_task import AbstractTask

#==============================================================================
class CollatzConjecture(AbstractTask):

    #--------------------------------------------------------------------------
    def receive_input(self):
        '''
        Specify and receive each piece of input the class will need from 
        the user to complete the task.
        '''
        print 'Collatz conjecture selected.'
        print 'Warning.  The Collatz conjecture is an unsolved mathematical problem.  Choosing smaller numbers is advised.'
        print ''
        print 'Please enter a starting number:'
        start = raw_input('Starting number: ')

        if self.validate_input(start):
            self._start = int(start)
            return True
        else:
            return False

    #--------------------------------------------------------------------------
    def validate_input(self, start):
        '''
        '''
        try:
            if not start.isdigit():
                print 'Starting number %s must be a number but it is not.' % (start)
                print 'Generating Collatz conjecture will abort.'
                return False

            start_number = int(start)
            if start_number < 1:
                print 'Collatz conjectures must start with positive intgers.'
                return False
            
            return True

        except:
            print 'Starting number %s must be a positive integer.' % start
            print 'Generating Collatz conjecture will abort.'
            return False

    #--------------------------------------------------------------------------
    def process(self):
        '''
        do all tasks needed to get the final result
        '''
        self.perform_collatz_conjecture(self._start)
        
    #--------------------------------------------------------------------------
    def perform_collatz_conjecture(self, number):

        self._output.append(number)

        if number == 1:
            return
        else:
            if number % 2 == 0:
                new_number = number / 2
            else:
                new_number = (number * 3) + 1

            self.perform_collatz_conjecture(new_number)

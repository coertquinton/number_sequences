'''
Created on 19 Jul 2016

@author: Quinton
'''
import abc

#==============================================================================
class AbstractTask(object):
    
    def __init__(self):
        '''
        '''
        self._output = []
        

    #--------------------------------------------------------------------------
    @abc.abstractmethod
    def receive_input(self):
        '''
        Specify and receive each piece of input the class will need from 
        the user to complete the task.
        '''

        return
    
    #--------------------------------------------------------------------------
    @abc.abstractmethod
    def process(self):
        '''
        do all tasks needed to get the final result
        '''
        
        return 
    
    #--------------------------------------------------------------------------
    def return_result(self):
        '''
        Return the output to the calling program.  The output should be a list of numbers
        '''
        
        return self._output
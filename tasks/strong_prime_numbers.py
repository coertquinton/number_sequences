'''
Created on 19 Jul 2016

@author: Quinton
'''

from prime_numbers import PrimeNumbers

#==============================================================================
class StrongPrimeNumbers(PrimeNumbers):

    #--------------------------------------------------------------------------
    def process(self):
        '''
        do all tasks needed to get the final result
        '''

        super(StrongPrimeNumbers, self).process()

        self.previous_prime_number(self._output[0])
        self.next_prime_number(self._output[len(self._output) - 1])

        self.select_strong_primes()

    #--------------------------------------------------------------------------
    def previous_prime_number(self, number):
        '''
        '''

        x = number
        while True:
            x -= 1
            if x <= 1:
                return

            if self.confirm_prime(x):
                self._output.insert(0, x)
                break

    #--------------------------------------------------------------------------
    def next_prime_number(self, number):
        '''
        '''

        x = number
        while True:
            x += 1
            if self.confirm_prime(x):
                self._output.append(x)
                break

    #--------------------------------------------------------------------------
    def select_strong_primes(self):
        '''
        Picks out all the strong primes and replaces those in the output list with them.
        '''
        strong_primes = []
        
        for x in range(1, len(self._output)-1):
            
            tested_prime = self._output[x]
            test_value = (self._output[x-1] + self._output[x+1]) / 2

            if tested_prime > test_value:
                strong_primes.append(tested_prime)

        self._output = strong_primes

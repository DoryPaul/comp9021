import sys
from math import sqrt


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    S=[]
    for i in range(n):
        if is_prime(i):
            S.append(i)
    largest_prime_strictly_smaller_than_n=S[-1]
        


    
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')



def is_prime(n):
    if n==1:
        return True
    if n==2:
        return True
    if n!=2 and n%2==0:
        return False
    for i in range(3,round(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

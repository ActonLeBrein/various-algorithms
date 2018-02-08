# Script text here

import random
from random import randint

def randlist(n):
    l = []
    while len(l) < n:
        v = randint(-n,n)
        if v not in l:
            l.append(v)
    return l  
    
def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result
              
print randlist(1000)  
print random_subset( randlist(1000), 1000 )
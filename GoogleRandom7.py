from random import randint

def random7():
    lis = [[1,2,3,4,5],
           [6,7,1,2,3],
           [4,5,6,7,1],
           [2,3,4,5,6],
           [7,0,0,0,0]]
    result = 0
    while result == 0:
        j = randint(0,4)
        i = randint(0,4)
        result = lis[i][j]
    return result
    
print random7()
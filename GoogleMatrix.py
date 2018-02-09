from random import randint

def matrix(n):
    m = []
    l = []
    while len(m) < n:
        while len(l) < n:
            v = randint(-n,n)
            l = l + [v]
        m = m + [l]
        l = []
    return m
    
def subsum(n):
    m = matrix(n)
    print m
    l = 2
    suma = 0
    x = 0
    y = 0
    i = l
    j = l
    max = [['suma',suma],['x1',x],['y1',y],['x2',i],['y2',j]]
    while l < len(m)-1:
        while j < len(m)-1:
            while i < len(m)-1:
                for a in range (y,j+1):
                    suma = suma + sum(m[a][x:i+1])
                if suma > max[0][1]:
                    max[0][1] = suma
                    max[1][1] = x
                    max[2][1] = y
                    max[3][1] = i
                    max[4][1] = j
                    i += 1
                    x += 1
                    suma = 0
                else:
                    i += 1
                    x += 1
                    suma = 0
            if suma > max[0][1]:
                max[0][1] = suma
                max[1][1] = x
                max[2][1] = y
                max[3][1] = i
                max[4][1] = j
                i = i - l
                x = x - l
                j += 1
                y += 1
                suma = 0
            else:
                i = i - l
                x = x - l
                j += 1
                y += 1
                suma = 0
        if suma > max[0][1]:
            max[0][1] = suma
            max[1][1] = x
            max[2][1] = y
            max[3][1] = i
            max[4][1] = j
            l += 1
            i = l
            j = l
            x = 0
            y = 0
            suma = 0
        else:
            l += 1
            i = l
            j = l
            x = 0
            y = 0
            suma = 0
    if suma > max[0][1]:
        max[0][1] = suma
        max[1][1] = x
        max[2][1] = y
        max[3][1] = i
        max[4][1] = j
    return max
    
print subsum(10)
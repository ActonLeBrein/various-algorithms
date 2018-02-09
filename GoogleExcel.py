# Script text here
import math

d1 = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,'K':11,'L':12,'M':13,
    'N':14,'P':15,'O':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
d2 = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J',10:'K',11:'L',12:'M',
    13:'N',14:'P',15:'O',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def excel(s):
    c = 0
    i = 0
    k = 0
    l = list(s)
    l.reverse()
    while i < len(l):
        c = c + d1[l[i]]*(math.pow(26,i))
        i += 1
    m = 0
    while m < c:
        if m < 26:
            print (d2[m], m)
            m += 1
        else:
            k = m
            j = ''
            while k >= 26:
                j = d2[math.fmod(k,26)] + j
                k = k/26
                k = k - 1
                if k < 26:
                    j = d2[k] + j
            print (j, m)
            m += 1
excel('ZZZ')
# Script text here
import math

balls = [1,1,1,2,1,1,1,1]

def ball(l,t):
    c = t
    if len(l) == 2:
        if l[0] > l[1]:
            print l[0]
        elif l[1] > l[0]:
            print l[1]
        else:
            print 'c is ', c
    else:
        if math.fmod(len(l),2) == 0:
            if sum(l[0:len(l)/2]) > sum(l[len(l)/2:len(l)]):
                ball(l[0:len(l)/2],c)
            else:
                ball(l[len(l)/2:len(l)+1],c)
        else:
            if l[0] > c:
                c = l[0]
            if len(l[1:len(l)]) == 2:
                if l[0] > l[1]:
                    print l[0]
                elif l[1] > l[0]:
                    print l[1]
                else:
                    print 'c is ', c
            elif sum(l[1:len(l)/2 + 1]) > sum(l[len(l)/2 + 1:len(l)]):
                ball(l[1:len(l)/2 + 1],c)
            else:
                ball(l[len(l)/2 + 1:len(l)],c)
                
ball(balls,0)

def divlist(l,m,r):
    i = len(l)
    j = 1
    road = r
    w = m
    while j < i:
        if len(l[0:j]) == 1:
            j += 1
        elif len(l[j:i]) == 1:
            j += 1
        else:
            if m != 2:
                if weightmatch(l[0:j]) and m < 2:
                    road = road + [[['LEFT path']+l[0:j]] + [l[j:i]]]
                    m += 1
                    divlist(l[0:j],m,road)
                    break
                elif weightmatch(l[j:i]) and m < 2:
                    road = road + [[l[0:j]] + [['RIGHT path']+l[j:i]]]
                    m += 1
                    divlist(l[j:i],m,road)
                    break
                else:
                    j += 1
                    m = 0
                    road = []
            else:
                road = road + [[l[0:j]] + [l[j:i]]]
                break
    print 'SUCCESS!!!! road:',road
            
def weightmatch(l):
    c = 0
    if math.fmod(len(l),2) != 0:
        c = l[0]
        if len(l[1:len(l)]) == 2:
            if l[0] != l[1]:
                return True
            elif l[1] != c:
                return True
            else:
                return False
    else:
        if sum(l[0:len(l)/2]) != sum(l[len(l)/2:len(l)]):
            return True
        else:
            return False

divlist(balls,0,[])
a = [2,4,2,5,6,7,1,1,12]
b = [1,2,3,2,1,5,2,4,3,4]
c = [3,2,1,2,3,1,1,1,2,2,3]
d = [5,1,7,8,3,4]
s = 25

def seq(a,s):
    lenmin = len(a)
    minseq = []
    i = 2
    a.sort()
    a.reverse()
    print a
    if a[0] > s:
        lenmin = len(a[0:2])
        minseq = a[0:2]
        return minseq, lenmin
    else:
        while i < len(a)+1:
            if sum(a[0:i]) > s:
                lenmin = len(a[0:i])
                minseq = a[0:i]
                return minseq, lenmin
            else:
                i += 1
print seq(a,s)
print seq(b,s)
print seq(c,s)
print seq(d,s)
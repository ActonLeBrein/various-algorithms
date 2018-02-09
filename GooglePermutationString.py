# Script text here

def permutation(s):
    l = list(s)
    p = {}
    n = 1
    i = 0
    j = 1
    while i < len(l):
        p[n] = l[i]
        n += 1
        i += 1
    i = 0
    while i < len(l):
        while j < n:
            if l[i] in p[j]:
                j += 1
            elif (l[i] + p[j]) in p.values():
                j += 1
            else:
                p[n] = l[i] + p[j]
                n += 1
                j += 1
                i = 0
        i += 1
        j = 1
    keys = p.keys()
    keys.sort()
    values = p.values()
    values.sort()
    i = 0
    l = []
    n -= 1
    print n
    while i < n:
        l = l + [[keys[i], values[i]]]
        i += 1
    return l
    
print permutation('abcd')
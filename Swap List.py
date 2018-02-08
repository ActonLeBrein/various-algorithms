a = [2,4,2,5,6,7,1,1,12]
b = [1,2,3,2,1,5,2,4,3,4]
c = [3,2,1,2,3,1,1,1,2,2,3]
d = [5,1,7,8,3,4]

def swap(a):
    i = 1
    a.sort()
    a.reverse()
    j = 0
    k = 0
    print a
    while i+1 < len(a):
        if a[i] == a[i+1]:
            i += 2
        else:
            j = a[i+1]
            k = a[i]
            a[i] = j
            a[i+1] = k
            i += 2
    return a

print swap(a)
print swap(b)
print swap(c)
print swap(d)
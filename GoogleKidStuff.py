# Script text here

a = [1,8,3,4,5,6,7,2,9,10,'a','h','c','d','e','f','g','b','i','j']

def intchart(l):
    print "initial list %s" % l
    integers = l[0:len(a)/2]
    integers.sort()
    chart = l[len(a)/2:len(a)]
    chart.sort()
    print "the list of integers %s" % integers
    print "the list of characters %s" % chart
    l = []
    i = 0
    while i < len(chart):
        l = l + [integers[i]] + [chart[i]]
        i += 1
    print "the resulting mixup of both list %s" % l
intchart(a)
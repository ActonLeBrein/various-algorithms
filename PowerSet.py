def list_powerset(lst):
    return reduce(lambda result,x: result + [subset+[x] for subset in result],lst,[[]])
print list_powerset([1,2,3,4,5])
#############################################################
def powersetlist(s):
    r = [[]]
    for e in s:
        print "r: %-55r e: %r" % (r,e)
        r += [x+[e] for x in r]
    return r
 
s= [0,1,2,3]    
print "\npowersetlist(%r) =\n  %r" % (s, powersetlist(s))
#############################################################
def p(l):
    if not l: return [[]]
    return p(l[1:]) + [[l[0]] + x for x in p(l[1:])]
print p([1,2,3])
#############################################################
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
 
print set(powerset({1,2,3,4}))
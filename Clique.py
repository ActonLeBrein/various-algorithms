# Script text here

graph = {'A': ['G','B','C','D','F','E'],
         'B': ['A','C','G','D'],
         'C': ['D','E','A','B','G','F'],
         'D': ['A','B','C','G','E','F'],
         'E': ['F','D','G','A','C'],
         'F': ['A','C','G','B','E','D'],
         'G': ['D','A','C','F','E']}

def check_node_in(g,n,c):
    i = 0
    while i < len(c):
        if (n in g[c[i]]) and (c[i] in g[n]):
            i += 1
        else:
            return False
            break
    return True
    
def combinations_by_subset(seq, r):
    if r:
        for i in xrange(r - 1, len(seq)):
            for cl in (list(c) for c in combinations_by_subset(seq[:i], r - 1)):
                cl.append(seq[i])
                yield tuple(cl)
    else:
        yield tuple()

def combination(s):
    k = len(s)
    l = []
    while k > 0:
        l = l + [''.join(c) for c in combinations_by_subset(s, k)]
        k -= 1
    for i in range(len(l)):
        l[i] = list(l[i])
    return l

###################################### CLIQUE ######################################
def clique(g):
    flag = True
    r = combination(g.keys())[:-1*(len(g.keys()))]
    c = []
    j = 0
    k = 0
    while j < len(r):
        while k < len(r[j]):
            if k == 0:
                if check_node_in(g,r[j][k],r[j][k+1:]) == False:
                    flag = False
                    break
                else:
                    k += 1
            elif k == len(r[j])-1:
                if check_node_in(g,r[j][k],r[j][:-1]) == False:
                    flag = False
                    break
                else:
                    k += 1
            else:
                if check_node_in(g,r[j][k],r[j][0:k] + r[j][k+1:]) == False:
                    flag = False
                    break
                else:
                    k += 1
        if flag:
            c = c + [r[j]]
            j += 1
            k = 0
        else:
            flag = True
            j += 1
            k = 0
    return c

print 'final result is %s' % (str(clique(graph)))

###################################### K_CLIQUE ######################################
def k_clique(g,n):
    flag = True
    r = combination(g.keys())[:-1*(len(g.keys()))]
    c = []
    j = 0
    k = 0
    while j < len(r):
        while k < len(r[j]):
            if k == 0:
                if check_node_in(g,r[j][k],r[j][k+1:]) == False:
                    flag = False
                    break
                else:
                    k += 1
            elif k == len(r[j])-1:
                if check_node_in(g,r[j][k],r[j][:-1]) == False:
                    flag = False
                    break
                else:
                    k += 1
            else:
                if check_node_in(g,r[j][k],r[j][0:k] + r[j][k+1:]) == False:
                    flag = False
                    break
                else:
                    k += 1
        if flag:
            if n == len(r[j]):
                c = c + [r[j]]
                j += 1
                k = 0
            else:
                j += 1
                k = 0
        else:
            flag = True
            j += 1
            k = 0
    if len(c) != 0:
        return c
    else:
        return 'there is no clique with value %s' % n

print 'K Clique result is: %s' % str(k_clique(graph,6))

###################################### BIG_CLIQUE ######################################
def big_clique(g):
    flag = True
    r = combination(g.keys())[:-1*(len(g.keys()))]
    c = []
    j = 0
    k = 0
    while j < len(r):
        while k < len(r[j]):
            if k == 0:
                if check_node_in(g,r[j][k],r[j][k+1:]) == False:
                    flag = False
                    break
                else:
                    k += 1
            elif k == len(r[j])-1:
                if check_node_in(g,r[j][k],r[j][:-1]) == False:
                    flag = False
                    break
                else:
                    k += 1
            else:
                if check_node_in(g,r[j][k],r[j][0:k] + r[j][k+1:]) == False:
                    flag = False
                    break
                else:
                    k += 1
        if flag:
            if len(c) < len(r[j]):
                c = r[j]
                j += 1
                k = 0
            else:
                j += 1
                k = 0
        else:
            flag = True
            j += 1
            k = 0
    return c

print 'Big Clique result is %s' % str(big_clique(graph))
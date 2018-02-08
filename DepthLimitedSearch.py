# Script text here

# Script text here

graph = {'A': ['B','C','E'],
         'B': ['A','C','D'],
         'C': ['D'],
         'D': ['C','I'],
         'E': ['F','D'],
         'F': ['C','G'],
         'G': ['H','I'],
         'H': ['G','C'],
         'I': ['A','G','D']}

def DLS(g,s,e,p,n):
    d = n
    path = p
    path = path + [s]
    tmp_path = g[s]
    i = 0
    l = list(set(path).intersection(set(tmp_path)))
    if len(l) != 0:
        while i < len(l):
            del tmp_path[tmp_path.index(l[i])]
            i += 1
    i = 0
    while i < len(tmp_path):
        if tmp_path[i] == e and d >= 0:
            path = path + [tmp_path[i]]
            print "VALID PATH ", path, d
            break
        else:
            print path + [tmp_path[i]], d
            DLS(g,tmp_path[i],e,path,d-1)
            i += 1

DLS(graph,'A','I',[],2)???
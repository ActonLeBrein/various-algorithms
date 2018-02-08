# Script text here

graph = {'A': ['B','C','E'],
         'B': ['A','C','D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F','D'],
         'F': ['C']}

def DFS(g,s,e,p):
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
        if tmp_path[i] == e:
            path = path + [tmp_path[i]]
            print "VALID PATH ", path
            break
        else:
            print path + [tmp_path[i]]
            DFS(g,tmp_path[i],e,path)
            i += 1

DFS(graph,'A','D',[])?
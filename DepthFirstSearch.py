# Script text here

graph = {'A': ['B','C','E'],
         'B': ['A','C','D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F','D'],
         'F': ['C']}

def DFS_recursive_1(g,s,e,p):
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
            DFS_recursive_1(g,tmp_path[i],e,path)
            i += 1

DFS_recursive_1(graph,'A','D',[])

def DFS_recursive_2(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        print path
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = DFS_recursive_2(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

DFS_recursive_2(graph,'A','D')

def DFS_iterative_1(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path+[next]
            else:
                stack.append((next, path + [next]))

print list(DFS_iterative_1(graph, 'A', 'F'))

class graphs():
  
  def __init__(self):
    self.graph={}
  
  def add_node(self,s,e):
    if s not in self.graph:
      self.graph[s]=[e]
    elif e not in self.graph[s]:
      self.graph[s]+=[e]
    else:
      pass

  def dfs_paths(self,graph, start, goal):
      stack = [(start, [start])]
      while stack:
          (vertex, path) = stack.pop()
          for next in set(graph[vertex]) - set(path):
              if next == goal:
                  yield path+[next]
              else:
                  stack.append((next, path + [next]))

a=graphs()
a.add_node('A','B')
a.add_node('A','C')
a.add_node('B','A')
a.add_node('B','D')
a.add_node('B','E')
a.add_node('C','A')
a.add_node('C','F')
a.add_node('D','B')
a.add_node('E','B')
a.add_node('E','F')
a.add_node('F','C')
a.add_node('F','E')
print a.graph
print list(a.dfs_paths(a.graph, 'A', 'F'))

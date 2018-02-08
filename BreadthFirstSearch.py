graph = {'A': ['B', 'C','E'],
         'B': ['A','C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F','D'],
         'F': ['C']}

class MyQUEUE: # just an implementation of a queue
	
	def __init__(self):
		self.holder = []
		
	def enqueue(self,val):
		self.holder.append(val)
		
	def dequeue(self):
		val = None
		try:
			val = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass
			
		return val	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result


path_queue = MyQUEUE() # now we make a queue


def BFS(graph,start,end,q):
	
	temp_path = [start]
	
	q.enqueue(temp_path)
	
	while q.IsEmpty() == False:
		tmp_path = q.dequeue()
		last_node = tmp_path[len(tmp_path)-1]
		print tmp_path
		if last_node == end:
			print "VALID_PATH : ",tmp_path
		for link_node in graph[last_node]:
			if link_node not in tmp_path:
				new_path = []
				new_path = tmp_path + [link_node]
				q.enqueue(new_path)

BFS(graph,"A","D",path_queue)

################################### MY OWN BFS ###################################

# Script text here

graph = {'A': ['B','C','E'],
         'B': ['A','C','D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F','D'],
         'F': ['C']}

def BFS(g,s,e,p):
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
            #path = path + [tmp_path[i]]
            print "VALID PATH", path + [tmp_path[i]]
            i += 1
        else:
            #BFS(g,tmp_path[i],e,path)
            print path + [tmp_path[i]]
            i += 1
    i = 0
    while i < len(tmp_path):
        BFS(g,tmp_path[i],e,path)
        i += 1

BFS(graph,'A','D',[])?
from random import randint

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data, pos):
        new_node = node() # create a new node
        new_node.data = data, pos
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.
    
    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next


def ranlist(n):
    d = {}
    l = []
    r = linked_list()
    i = 0
    v = 0
    while len(d.values()) < n:
        v = randint(-n,n)
        if not d.get(v):
            d[v] = v
    l = d.values()
    while i < len(l):
        r.add_node(l[i], 'pos' + str(i+1))
        i = i + 1
    return r

def circle(m):
    lis = ranlist(m)
    node = lis.cur_node
    first = node.data
    node = node.next
    while node:
        if node.data[0] < first[0]:
            first = node.data
            node = node.next
        else:
            node = node.next
    return 'The less value is '+str(first[0])+' in '+str(first[1])

ll = linked_list()
ll.add_node(1,0)
ll.add_node(2,1)
ll.add_node(3,2)
ll.add_node(4,3)
ll.list_print()
print circle(20)
ranlist(10).list_print()

def ranlist(n):
    d = {}
    l = []
    r = []
    i = 0
    v = 0
    while len(d.values()) < n+1:
        v = randint(0,n)
        if not d.get(v):
            d[v] = v
    l = d.values()
    while i < len(l):
        r = r + [[i, l[i], i + 1]]
        i = i + 1
    r[i-1] = [i-1, l[i-1], 0]
    return r

def circle(m):
    lis = ranlist(m)
    print(lis)
    print('length list '+len(lis))
    i = randint(0,m-1)
    j = i
    ans = lis[i]
    print('start point '+i)
    less = lis[i][1]
    i = i + 1
    while j != lis[i][0]:
        if i == len(lis)-1:
            if less > lis[i][1]:
                less = lis[i][1]
                ans  = lis[i]
                i = 0
            else:
                i = 0
        elif less > lis[i][1]:
            less = lis[i][1]
            ans  = lis[i]
            if lis[i][0] == len(lis)-1:
                i == 0
            else:
                i = i + 1
        else:
            i = i + 1
    print('less '+less)
    return ans, less
print(circle(100))
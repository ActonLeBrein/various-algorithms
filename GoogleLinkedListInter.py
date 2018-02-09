# Script text here

from random import randint

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next
    
    def len_list(self):
        node = self.cur_node # cant point to ll!
        i = 0
        while node:
            i += 1
            node = node.next
        return i
    
    def has_data(self, data):
        node = self.cur_node # cant point to ll!
        while node:
            if data == node.data:
                return True
            else:
                node = node.next
        return False
    
    def get_data(self, data):
        if self.has_data(data):
            node = self.cur_node # cant point to ll!
            while node:
                if data == node.data:
                    return node.data
                else:
                    node = node.next
        else:
            return None
        
    def pos_data(self, pos):
        node = self.cur_node
        if pos == 0:
            return node.data
        else:
            while pos > 0:
                node = node.next
                pos -= 1
            return node.data

def interlinklist(n,m):
    i = 0
    r = []
    l = []
    while i < n.len_list():
        l = l + [n.pos_data(i)]
        i += 1
    i = 0
    while i < m.len_list():
        if m.pos_data(i) in l:
            r = r + [m.pos_data(i)]
            i += 1
        else:
            l = l + [m.pos_data(i)]
            i += 1
    l.sort()
    r.sort()
    print "Union list is %s and intersection is %s" % (l,r)

def randomlinklist(k):
    n = k
    ln = linked_list()
    o = 0
    while k > 0:
        o = randint(-n,n)
        if not ln.has_data(o):
            ln.add_node(o)
            k -= 1
    return ln
    
a = randomlinklist(15)
print 'list a '
a.list_print()
b = randomlinklist(20)
print 'list b'
b.list_print()
interlinklist(a,b)
interlinklist(b,a)
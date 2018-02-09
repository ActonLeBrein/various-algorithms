# Script text here

import random
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

def linklist(n):
    i = 0
    ln = []
    while len(ln) < n+1:
        i = randint(1,n+1)
        l = linked_list()
        while i > 0:
            l.add_node(randint(-n,n))
            i -= 1
        ln.append(l)
    return ln

def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result        

def random_select(l,k):
    r = []
    N = 0
    for i in l:
        N += 1
        if len(r) < k:
            r.append(i.pos_data(randint(0,i.len_list()-1)))
        else:
            s = int(random.random() * N)
            if s < k:
                r[s] = i.pos_data(randint(0,i.len_list()-1))
    return r

v = linklist(500)
'''
for i in v:
    print "number of elements is ", i.len_list()
    print "last pos is ", i.pos_data(i.len_list() - 1)
    i.list_print()'''
    
print "the random list from a linked list is ", random_select(v,100), len(random_select(v,100))
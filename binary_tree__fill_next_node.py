class binary_tree():
  
  def __init__(self):
    self.root=None
    self.tmp_root=None
    self.tree={}

  def add_node(self,value,side):
    if value not in self.tree and len(self.tree)==0:
      self.root=value
      self.tree[value]={'left':None,'right':None,'next_node':None}
    elif value not in self.tree:
      self.tmp_root=self.root
      while self.tmp_root is not None:
        if self.tree[self.tmp_root]['left'] is None:
          self.tree[self.tmp_root]['left']=value
          self.tree[value]={'left':None,'right':None,'next_node':None}
          self.tmp_root=None
        elif self.tree[self.tmp_root]['right'] is None:
          self.tree[self.tmp_root]['right']=value
          self.tree[value]={'left':None,'right':None,'next_node':None}
          self.tmp_root=None
        else:
          self.tmp_root=self.tree[self.tmp_root][side]
    else:
      pass
  
  def fill_next_node(self,root):
    if self.tree[root]['left'] is not None or self.tree[root]['right'] is not None:
      self.tree[self.tree[root]['left']]['next_node']=self.tree[root]['right']
      self.fill_next_node(self.tree[root]['left'])
      self.fill_next_node(self.tree[root]['right'])
    
t=binary_tree()
t.add_node('A','left')
t.add_node('B','left')
t.add_node('C','right')
t.add_node('D','left')
t.add_node('E','right')
t.add_node('F','left')
t.add_node('G','right')
t.fill_next_node(t.root)
print t.tree,t.root

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left: root.right.next = tmp.left; break
                    if tmp.right: root.right.next = tmp.right; break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left: root.left.next = tmp.left; break
                    if tmp.right: root.left.next = tmp.right; break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left: root.right.next = tmp.left; break
                    if tmp.right: root.right.next = tmp.right; break
                    tmp = tmp.next
            self.connect(root.right)
            self.connect(root.left)
            # @connect(root.right)should be the first!!!

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            p = root; q = None; nextNode = None
            while p:
                if p.left:
                    if q: q.next = p.left
                    q = p.left
                    if nextNode == None: nextNode = q
                if p.right:
                    if q: q.next = p.right
                    q = p.right
                    if nextNode == None: nextNode = q
                p = p.next
            self.connect(nextNode)

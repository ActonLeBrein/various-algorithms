# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        return self.flattenRecu(root, None)
        
    def flattenRecu(self, root, list_head):
        if root != None:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head
        
class Solution2:
    list_head = None
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
            return root
        
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
result = Solution().flatten(root)
print result.val
print result.right.val
print result.right.right.val
print result.right.right.right.val
print result.right.right.right.right.val
print result.right.right.right.right.right.val


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traverse(head,result):
    if head is not None:
        inorder_traverse(head.left,result)
        result.append(head.data)
        inorder_traverse(head.right,result)


"""
Constructing below tree
           5
         /   \
        3     6
       / \     \
      1   4     8
     / \       / \
    0   2     7   9  
"""
# Create the above Tree
head = Node(5)

head.left = Node(3)
head.left.left = Node(1)
head.left.right = Node(4)
head.left.left.left = Node(0)
head.left.left.right = Node(2)

head.right = Node(6)
head.right.right = Node(8)
head.right.right.left = Node(7)
head.right.right.right = Node(9)

# result will store the output
result = []
inorder_traverse(head, result)

print("Extracted Double Linked list is")
print(' '.join(str(res) for res in result))
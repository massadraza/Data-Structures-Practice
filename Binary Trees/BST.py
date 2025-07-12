# Learning about Binary Search Tree (BST)
# They are different from binary trees since they follow the BST property

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        self.insert_helper(self.root, new_value)

    def insert_helper(self, curr, new_value):
        if curr.data < new_value:
            if curr.right:
                self.insert_helper(curr.right, new_value)
            else:
                curr.right = Node(new_value)
        else:
            if curr.left:
                self.insert_helper(curr.left, new_value)
            else:
                curr.left = Node(new_value)

    def search(self, find_value):
        return self.search_helper(self.root, find_value)
    
    def search_helper(self, curr, find_value):
        if curr:
            if curr.data == find_value:
                return True
            elif curr.data < find_value:
                return self.search_helper(curr.right, find_value)
            else:
                return self.search_helper(curr.left, find_value)
            
    # Challenge: Create a method that will check whether the tree follows the BST property

    def is_bst_satisfied(self):
         def helper(node, lower=float('-inf'), upper=float('inf')):
             if not node:
                 return True
             
             val = node.data
             if val <= lower or val >= upper:
                 return False
             if not helper(node.right, val, upper):
                 return False
             if not helper(node.left, lower, val):
                 return False
             return True
         
         return helper(self.root)
        
bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
#bst.insert(1335)

#print(bst.search(9))    
#print(bst.search(14))    
#print(bst.search(2345))    

anotherTree = BST(1)
anotherTree.root.left = Node(2)
anotherTree.root.right = Node(3)
anotherTree.root.left.left = Node(4)

print(bst.is_bst_satisfied())
print(anotherTree.is_bst_satisfied())
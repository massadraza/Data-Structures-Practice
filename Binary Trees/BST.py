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
                return self.search_helper
            else:
                return self.search_helper(curr.left, find_value)
        

    
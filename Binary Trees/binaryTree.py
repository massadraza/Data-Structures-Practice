# Massad Raza
# Learning about binary search trees and the variety of ways to traverse them


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    

class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s
    

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):

        if start:
            traversal = traversal + (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = traversal + (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):

        if start: 
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal = traversal + (str(start.value) + "-")
        return traversal
    
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal = traversal + str(queue.peek()) + "-"
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    def reverse_levelorder_print(self, start):
        if start is None:
            return 
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal = traversal + str(node.value) + "-"

        return traversal
    
    def height(self, node):
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)
    
    # Challenge, calculate size of a tree

    def size_(self, node):

        if self.root is None:
            return 0
        
        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size = size + 1
                stack.push(node.left)
            if node.right: 
                size = size + 1
                stack.push(node.right)

        return size



    
# Functions to test binary tree

myTree = BinaryTree(1)
myTree.root.left = Node(2)
myTree.root.right = Node(3)
myTree.root.left.left = Node(4)
myTree.root.left.right = Node(5)


print(myTree.size_(myTree.root))

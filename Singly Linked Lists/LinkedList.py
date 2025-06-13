# Implementing singly linked lists in python 
# Massad Raza

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
 
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_Node
   
    
    def prepend(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_Node = Node(data)

        new_Node.next = prev_node.next
        prev_node.next = new_Node


testList = LinkedList()

testList.append("A")
testList.print_list()
print("-----------")
testList.append("B")
testList.append("C")
testList.append("D")
testList.print_list()
testList.prepend("I")
print("-----------")
testList.print_list()
testList.insert_after_node(testList.head.next, "8")
print("-----------")
testList.print_list()





        


    






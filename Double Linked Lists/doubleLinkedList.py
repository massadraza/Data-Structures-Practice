class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur


    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
                return
            cur = cur.next
    
    def delete(self, key):
        cur = self.head
        
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
            else:
                nxt = cur.next
                cur.next = None
                nxt.prev = None
                cur = None
                self.head = nxt
                return
            cur = cur.next
        
# Functions to practice double linked lists

doubleLIST = DoublyLinkedList()

doubleLIST.append(1)
doubleLIST.append(2)
doubleLIST.append(3)
doubleLIST.append(4)
doubleLIST.append(5)
doubleLIST.append(6)

doubleLIST.print_list()
                
print("-----------")

doubleLIST.delete(1)
doubleLIST.delete(4)
doubleLIST.delete(3)
doubleLIST.print_list()
    

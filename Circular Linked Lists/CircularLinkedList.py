# By: Massad Raza


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next
            

    # Attempt to split linked lists using this method

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count
        
    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head
        
        mid = size // 2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        splitCircularList = CircularLinkedList()

        while cur.next != self.head:
            splitCircularList.append(cur.data)
            cur = cur.next
        splitCircularList.append(cur.data)

        self.print_list()
        print("          ")
        splitCircularList.print_list()


    # Is Circular LinkedList Exercise

    def is_circular_linked_list(self, input_list):
        if input_list.head:
            cur = input_list.head
            while cur.next:
                cur = cur.next
                if cur.next == input_list.head:
                    return True
                return False
        else:
                return False
        

# Functions to test circular linked list

circularList = CircularLinkedList()

circularList.append("A")
circularList.append("B")
circularList.append("C")
circularList.append("D")
circularList.prepend("1")
circularList.prepend("2")
circularList.split_list()
print(" ")

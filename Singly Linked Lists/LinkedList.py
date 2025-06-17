# Implementing singly linked lists in python 
# Created by Massad Raza

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

    def delete_node(self, key):

        cur_Node = self.head

        if cur_Node and cur_Node.data == key:
            self.head = cur_Node.next
            cur_Node = None
            return
        
        prev = None
        while cur_Node and cur_Node.data != key:
            prev = cur_Node
            cur_Node = cur_Node.next

        if cur_Node is None:
            return
        
        prev.next = cur_Node.next
        cur_Node = None

    def delete_node_at_pos(self, pos):

        # When position is 0

        if self.head:
            cur_Node = self.head

            if pos == 0:
                self.head = cur_Node.next
                cur_Node = None
        
        # When position is NOT 0

        prev = None
        counter = 0

        while cur_Node and counter != pos:
            prev = cur_Node
            cur_Node = cur_Node.next
            counter = counter + 1
        
        if cur_Node is None:
            return
        
        prev.next = cur_Node.next
        cur_Node = None

    def len_iterative(self):
        counter = 0

        cur_Node = self.head

        while cur_Node:
            counter = counter + 1
            cur_Node = cur_Node.next
        return counter
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap_nodes(self, key1, key2):

        if key1 == key2:
            return
        
        prev1 = None
        cur_1 = self.head

        while cur_1 and cur_1.data != key1:
            prev1 = cur_1
            cur_1 = cur_1.next

        prev2 = None
        cur_2 = self.head

        while cur_2 and cur_2.data != key2:
            prev2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return
        # Cannot conduct swap if one of the key's do not exist
        
        # The actual swapping of elements

        if prev1: 
            prev1.next = cur_2
        else:
            self.head = cur_2

        if prev2:
            prev2.next = cur_1
        else:
            self.head = cur_1
    

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_iterative(self):

        prev = None
        cur_Node = self.head

        while cur_Node:
            nxt = cur_Node.next
            cur_Node.next = prev
            prev = cur_Node
            cur_Node = nxt

        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, l_list):
        # takes in two linked lists, self and l_list labeled respectively

        p = self.head
        q = l_list.head
        s = None

        # handle situation when either linked list is empty

        if not p:
            return q
        if not q:
            return p
        

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            newHead = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        
        if not q:
            s.next = p

        self.head = newHead

        return self.head
    
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):

        totalLength = self.len_iterative()

        cur = self.head

        while cur: 
            if totalLength == n:
               # print(cur.data)
                return cur.data
            totalLength = totalLength - 1
            cur = cur.next

        if cur is None:
            return
        
    def count_occurrences_iterative(self, data):
        count = 0
        cur = self.head

        while cur:
            if cur.data == data:
                count = count + 1
            cur = cur.next
        return count
    
    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)
        

    def rotate(self, k):
        # Rotating a linked list around a specified pivot point k

        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            counter = 0

            while p and counter < k:
                prev = p
                p = p.next
                q = q.next
                counter = counter + 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_Palindrome_String(self):
        s = ""
        p = self.head
        
        while p:
            s = s + p.data
            p = p.next
        
        return s == s
    
    # Challenge Question 1: Move Tail to Head
    # Modify pointers using next

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last_Node = self.head
            prev = None
            while last_Node.next:
                prev = last_Node
                last_Node = last_Node.next
            last_Node.next = self.head
            prev.next = None
            self.head = last_Node

        



    







#-----Testing the LinkedList Methods-----#
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
testList.delete_node("A")
print("-----------")
testList.print_list()
print("-----------")
print("Length calculated iteratively:")
print(testList.len_iterative())
print("Length calculated recursively:")
print(testList.len_recursive(testList.head))

testList.swap_nodes("I", "C")
print("-----------")
print("NEW LIST")

newList = LinkedList()

newList.append("A")
newList.append("B")
newList.append("C")
newList.append("D")
newList.print_list()
print("____________________")

newList.reverse_iterative()
newList.print_list()
print("__________________")
newList.reverse_recursive()
newList.print_list()

# Practice merging linked lists

print("------------------------")

numbersOne = LinkedList()

numbersOne.append(1)
numbersOne.append(5)
numbersOne.append(7)
numbersOne.append(9)
numbersOne.append(10)

numbersTwo = LinkedList()
numbersTwo.append(2)
numbersTwo.append(3)
numbersTwo.append(4)
numbersTwo.append(6)
numbersTwo.append(8)

numbersOne.merge_sorted(numbersTwo)
numbersOne.print_list()

duplicatedList = LinkedList()
duplicatedList.append(1)
duplicatedList.append(2)
duplicatedList.append(3)
duplicatedList.append(4)
duplicatedList.append(1)
duplicatedList.append(5)

print("----------------------------")

print("List before duplicates are removed")
duplicatedList.print_list()
print("List after duplicates removed")
duplicatedList.remove_duplicates()
duplicatedList.print_list()
print("---------------")
print(duplicatedList.print_nth_from_last(4))
print(duplicatedList.print_nth_from_last(3))
print("-------------------")
print(duplicatedList.count_occurrences_iterative(2))
print("-------------")

rotatingList = LinkedList()

rotatingList.append(1)
rotatingList.append(2)
rotatingList.append(3)
rotatingList.append(4)
rotatingList.append(5)
rotatingList.append(6)
rotatingList.append(7)
rotatingList.append(8)

rotatingList.rotate(4)
rotatingList.print_list()











        


    






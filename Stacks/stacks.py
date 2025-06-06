# Learning the Data Structure Stacks
# Methods: Push, Pop, Peek
# Massad Raza

class StackMethods():
    def __init__(self):
        self.books = []

    def push(self, book):
        self.books.append(book)

    def pop(self):
        return self.books.pop()
    
    def displayStack(self):
        return self.books
    
    def noneRemaining(self):
        return self.books == []
    
    def peek(self):
        if not self.noneRemaining():
            return self.books[-1]
        

# -1 refers to the most recent item added to the list

# Declare testStack object
testStack = StackMethods()

# Testing operations on a stack
testStack.push("Hey")
testStack.push("Hello")
testStack.push("Welcome")
print(testStack.displayStack())
testStack.pop()
print(testStack.displayStack())
testStack.pop()
print(testStack.displayStack())


newStack = StackMethods()
newStack.push(123)
newStack.push(1234)
newStack.push(12345)
print(newStack.displayStack())
print(newStack.peek())

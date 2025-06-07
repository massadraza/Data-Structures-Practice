# Made by: Massad Raza
# Using the data structures stacks to determine if brackets are balanced

#Create Stack class

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
# Determining whether parenthesis are balanced with this function
    
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    

def is_match(b1, b2):
    if b1 == "(" and b2 == ")":
        return True
    elif b1 == "{" and b2 == "}":
        return True
    elif b1 == "[" and b2 == "]":
        return True
    else:
        return False
    
print(is_paren_balanced("((({{}})))"))
print(is_paren_balanced("[]["))

# Analyzing test cases
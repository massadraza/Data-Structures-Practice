from stack import Stack

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    newString = ""

    while not stack.is_empty():
        newString = newString + stack.pop()
    
    return newString


input = "!olleh"
a = Stack()

print(reverse_string(a, input))

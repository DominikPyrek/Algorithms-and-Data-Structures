from collections import deque 
word = "Test"
stack = deque()

class Stack:
    def __init__(self):
        self.stack = deque()

    def pop(self):
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

def stringReversalUsingStack(string):
    stackOfString = Stack()

    for x in string:
        stackOfString.push(x)

    reversedString = ""
    while stackOfString.size() != 0:
        reversedString += stackOfString.pop()
    
    return reversedString



print(stringReversalUsingStack(word))

"""

Min Stack

Design a stack class that supports the push, pop, top and getMin operations. 

- MinStack() initializes the stack object
- def push() pushes the element val onto the stack 
- def pop() removes the element on the top of the stack 
- int top() gets the top element of the stack 
- int getMin() retrieves the minimum element in the stack 

Each function should run O(1) time. 

"""

class MinStack: 
    
    def __init__(self): 
        self.stack = []
        self.minstack = []
    
    def push(self, val:int) -> None: 
        self.minstack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    
    def pop(self) -> None: 
        self.stack.pop()
        self.minstack.pop()
    
    def top(self) -> int: 
        return self.stack[-1]
    
    def getMin(self) -> int: 
        return self.minstack[-1]

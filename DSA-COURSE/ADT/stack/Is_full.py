class Stack:
    def __init__(self) -> None:

        self.items = [0 for i in range(10)]

        self.count = 0

    def is_full(self):
        return self.count == len(self.items)
    
    def is_empty(self):
        return self.count == 0
    
    def push(self,item):
        if not self.is_full():
            self.items[self.count] = item
            self.count +=1
        else:
            raise IndexError("stack over_flow")
        
    def peek(self,item):
        if not self.is_empty():
            self.items[self.count] = item
            self.count -= 1
        else:
            raise IndexError("stack under flow")
        
    def pop(self):
        if not self.is_empty():
            self.count -=1
            a = self.items[self.count]
            self.items[self.count] = 0
            return a
        else:
            raise IndexError("stack under flow")
        
stack = Stack()
stack.push(331)
stack.push(332)
stack.push(333)
stack.push(334)
stack.push(335)

stack.pop()
stack.pop()
stack.pop()
stack.peek(2323)
print(stack.items)


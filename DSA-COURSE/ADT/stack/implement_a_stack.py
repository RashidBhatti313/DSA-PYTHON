class Stack:
    def __init__(self) -> None:
        self.items = [0 for i in range(10)]
        self.count = 0

    def is_full(self):
        return self.count == len(self.items)
    
    def is_empty(self):
        return self.count == 0
    
    def push(self, item):
        if not self.is_full():
            self.items[self.count] = item
            self.count += 1
        else:
            raise IndexError("Stack Over_ _ _ _....")
        
    def pop(self):
        if not self.is_empty():
            self.count -=  1
            a = self.items[self.count]
            self.items[self.count] = 0
            return 0
        else:
            raise IndexError("Stack Under-flow_ _ _ _....")
        
stack = Stack()
stack.push(333)
stack.push(444)
stack.push(555)
stack.push(666)
stack.push(777)
stack.push(888)
stack.push(999)
stack.push(1010)
stack.push(1111)
stack.push(1212)
# stack.push(1313)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.items)
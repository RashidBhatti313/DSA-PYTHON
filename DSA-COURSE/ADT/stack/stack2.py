class Stack:
    def __init__(self) -> None:
        self.items = []
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def push(self, item):
        self.items.append(item)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            e = self.items.pop()
            return e
        else:
            raise IndexError("stack UnderFlow")
        
    def peek(self):
        if not self.is_empty():
            return self.items[self.count - 1]
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return self.count
    
stack = Stack()
stack.push(121)
stack.push(131)
stack.push(141)
stack.push(151)
stack.push(161)
stack.push(171)


class Stack:
    def __init__(self) -> None:
        self.item = []
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def push(self, e):
        self.item.append(e)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            g = self.item.pop()
            return g
        else:
            raise IndexError("Stack is Underflow......")
        
    def peek(self):
        if not self.is_empty():
            return self.item[self.count - 1]
        else:
            raise IndexError("Stack is Ourflow.......")
        
stack = Stack()
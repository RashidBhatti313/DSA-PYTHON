class Stack:
    def __init__(self) -> None:
        self.items = []  # Corrected attribute name
        self.count = 0
    
    def is_empty(self):
        return self.count == 0
    
    def push(self, item):
        self.items.append(item)  # Use append to add items to the list
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            e = self.items.pop()  # Use pop to remove and return the last item
            return e
        else:
            raise IndexError("stack underflow")
        
    def peek(self):
        if not self.is_empty():
            return self.items[self.count - 1]
        else:
            raise IndexError("stack is empty")
    
    def size(self):
        return self.count

stack = Stack()
stack.push(44)
stack.push(424)
stack.push(43454)
stack.push(434)
print(stack.pop())
print(stack.pop())
print(stack.peek())
stack.push(44)
print(stack.size())
print(stack.peek())

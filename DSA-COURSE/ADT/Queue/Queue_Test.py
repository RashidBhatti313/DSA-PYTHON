class Queue:
    def __init__(self) -> None:
        self.items = [0 for i in range(5)]
        self.en_queue = -1
        self.de_queue = -1
        self.count = 0

    def is_full(self):
        return self.count == len(self.items)
    
    def is_empty(self):
        return self.count == 0
    
    def En_Queue(self, item):
        if not self.is_full():
            self.en_queue = (self.en_queue + 1) % len(self.items)
            self.items[self.en_queue] = item
            self.count += 1
        else:
            raise IndexError("Queue is Full.....")
        
    def De_Queue(self):
        if not self.is_empty():
            self.de_queue = (self.de_queue + 1) % len(self.items)
            data = self.items[self.de_queue]
            self.items[self.de_queue] = 0
            self.count -= 1
            return data
        else:
            raise IndexError("Queue is Underflow.....")
        
queue = Queue()
queue.En_Queue(34)
queue.En_Queue(44)
queue.De_Queue()

print(queue.items)

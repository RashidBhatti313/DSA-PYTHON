class Queue:
    def __init__(self):
        self.items = [0 for _ in range(5)]
        self.en = -1
        self.d = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.items)

    def en_queue(self, e):
        if not self.is_full():
            self.en = (self.en + 1) % len(self.items)
            self.items[self.en] = e
            self.count += 1
        else:
            raise IndexError("Queue is full")

    def de_queue(self):
        if not self.is_empty():
            self.d = (self.d + 1) % len(self.items)
            data = self.items[self.d]
            self.items[self.d] = 0
            self.count -= 1
            return data
        else:
            raise IndexError("Queue is empty")

# Example usage:
queue = Queue()
print(queue.items)
queue.en_queue(444)
queue.en_queue(555)
queue.en_queue(666)
queue.en_queue(777)
queue.en_queue(888)
print(queue.items)
queue.de_queue()
queue.de_queue()
queue.de_queue()
print(queue.items)
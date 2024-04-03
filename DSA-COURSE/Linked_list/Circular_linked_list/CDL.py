class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return (self.head is None) or (self.count == 0)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            last_node.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.tail
            new_node.next = self.head
            new_node.prev = last_node
            last_node.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def insert_at_specific_value(self, data, e):
        if not self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            x = self.search(e)
            newnode = Node(data)
            newnode.next = x.next
            newnode.prev = x
            newnode.next.prev = newnode
            x.next = newnode

    def display(self):
        if not self.head:
            print("Circular Doubly Linked List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data, end=" <-> ")
                temp = temp.next
                if temp == self.head:
                    break
            print()
    
    def search(self, e):
        if self.head is None:
            return None
        x = self.head
        while True:
            if (x.data == e):
                return x     
            x = x.next
            #agr ni milta
            if x == self.head:
                return None


# Example Usage:
circular_doubly_linked_list = CircularDoublyLinkedList()

circular_doubly_linked_list.insert_at_beginning(1)
circular_doubly_linked_list.insert_at_beginning(2)
circular_doubly_linked_list.insert_at_tail(3)
circular_doubly_linked_list.insert_at_tail(4)
circular_doubly_linked_list.insert_at_specific_value(3, 45)

print("Circular Doubly Linked List:")
circular_doubly_linked_list.display()
print(circular_doubly_linked_list.search(3).data)



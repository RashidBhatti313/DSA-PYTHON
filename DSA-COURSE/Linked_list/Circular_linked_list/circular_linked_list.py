class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class Circular_Linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return (self.head is None) or (self.count == 0)
    
    def insert_at_first(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode   
            self.tail = newnode
            newnode.next = newnode
            newnode.previous = newnode
        else: 
            last_node = self.head.previous
            newnode.next = self.head
            newnode.previous = last_node
            last_node.next = newnode
            self.head.previous = newnode
            self.tail = newnode

    def display(self):
        if not self.head:
            print("Circular Doubly Linked List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data)

                temp = temp.next
                if temp == self.head:
                    break
            print()


Clist = Circular_Linked_list()
Clist.is_empty()
Clist.insert_at_first(111)
Clist.insert_at_first(222)
Clist.insert_at_first(333)
Clist.display()
Clist.tail.data
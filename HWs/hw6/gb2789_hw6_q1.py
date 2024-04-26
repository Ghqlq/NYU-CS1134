#Question 1 
from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, elem):
        self.data.add_last(elem)
        self.n+=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.n-=1
        return self.data.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data

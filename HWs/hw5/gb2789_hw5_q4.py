
#Question 4

from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

class Queue:

    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()
        self.n = 0

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return not self.stack1 or self.stack2

    def enqueue(self, val):
        self.stack1.push(val)
        self.n += 1

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        self.n -= 1
        return self.stack2.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.stack2.is_empty():
            for i in range(len(self.stack1)):
                self.stack2.push(self.stack1.pop())
        return self.stack2.top()

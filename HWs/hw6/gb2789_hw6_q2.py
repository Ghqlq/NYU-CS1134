
#question 2

from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(int(num_str[i]))
        while self.data.header.next.data == 0 and len(self.data) > 1:
            self.data.delete_first()
            
    def __repr__(self):
        start = self.data.header.next
        new = ""
        while start.data is not None:
            new += str(start.data)
            start = start.next
        return new


    def __add__(self, other):
        new = Integer("")
        start1 = self.data.trailer.prev
        start2 = other.data.trailer.prev
        hold = 0
        while start1.data is not None and start2.data is not None:
            result = start1.data + start2.data + hold
            new.data.add_first(result%10)
            hold = result//10
            start1 = start1.prev
            start2 = start2.prev
        if start1.data is not None:
            long_cursor = start1
        else:
            long_cursor = start2
        while long_cursor.data is not None:
            new.data.add_first((long_cursor.data + hold) % 10)
            hold = (long_cursor.data + hold) // 10
            long_cursor = long_cursor.prev
        if hold != 0:
            new.data.add_first(hold)
        return new

    def __mul__(self, other):
        new = Integer("")
        start1 = self.data.trailer.prev
        for i in range(len(self.data)):
            start2 = other.data.trailer.prev
            hold = 0
            product = Integer("")
            for j in range(len(other.data)):
                result = start1.data * start2.data + hold
                product.data.add_first(result%10)
                hold = result//10
                start2 = start2.prev
            if hold != 0:
                product.data.add_first(hold)
            for j in range(i):
                product.data.add_last(0)
            new = new + product
            start1 = start1.prev
        while new.data.header.next.data == 0 and len(new.data) > 1:
            new.data.delete_first()
        return new





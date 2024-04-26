
#question 3

from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        if len(orig_str) == 0: #for initializing empty compactstring
            return
        count = 1
        for i in range(1, len(orig_str)):
            if orig_str[i] == orig_str[i - 1]:
                count += 1
            else:
                self.data.add_last((orig_str[i - 1], count))
                count = 1
        self.data.add_last((orig_str[len(orig_str) - 1], count))
    
    def __add__(self, other):
        new = CompactString("")
        start = self.data.header.next
        while start.next.data is not None:
            new.data.add_last(start.data)
            start = start.next
        if start.data[0] == other.data.header.next.data[0]:
            new.data.add_last(
                (start.data[0], start.data[1] + other.data.header.next.data[1]))
            start = other.data.header.next.next
        else:
            new.data.add_last(start.data)
            start = other.data.header.next
        while start.data is not None:
            new.data.add_last(start.data)
            start = start.next
        return new

    def __lt__(self, other):
        start1 = self.data.header.next
        start2 = other.data.header.next
        while start1.data == start2.data and start1.data is not None:
            start1 = start1.next
            start2 = start2.next
        if start1.data is None and start2.data is None:
            return False
        elif start1.data is None: #and start2.data is not None
            return True
        elif start2.data is  None: #and start1.data is not None
            return False
        else:
            if start1.data[0] == start2.data[0]:
                if start1.data[1] > start2.data[1]:
                    if start2.next.data is None:
                        return False
                    return start1.data[0] < start2.next.data[0]
                else:
                    if start1.next.data is None:
                        return True
                    return start1.next.data[0] < start2.data[0]
            return start1.data[0] < start2.data[0]


    def __le__(self, other):
        start1 = self.data.header.next
        start2 = other.data.header.next
        while start1.data == start2.data and start1.data is not None:
            start1 = start1.next
            start2 = start2.next
        if start1.data is None and start2.data is None:
            return True
        elif start1.data is None: #and start2.data is not None
            return True
        elif start2.data is None: #and start1.data is not None
            return False
        else:
            if start1.data[0] == start2.data[0]:
                if start1.data[1] > start2.data[1]:
                    if start2.next.data is None:
                        return False
                    return start1.data[0] < start2.next.data[0]
                else:
                    if start1.next.data is None:
                        return True
                    return start1.next.data[0] < start2.data[0]
            return start1.data[0] < start2.data[0]



    def __gt__(self, other):
        start1 = self.data.header.next
        start2 = other.data.header.next
        while start1.data == start2.data and start1.data is not None:
            start1 = start1.next
            start2 = start2.next
        if start1.data is None and start2.data is None:
            return False
        elif start1.data is None: #and start2.data is not None
            return False
        elif start2.data is None: #and start1.data is not None
            return True
        else:
            if start1.data[0] == start2.data[0]:
                if start1.data[1] > start2.data[1]:
                    if start2.next.data is None:
                        return True
                    return start1.data[0] > start2.next.data[0]
                else:
                    if start1.next.data is None:
                        return False
                    return start1.next.data[0] > start2.data[0]
            return start1.data[0] > start2.data[0]

    def __ge__(self, other):
        start1 = self.data.header.next
        start2 = other.data.header.next
        while start1.data == start2.data and start1.data is not None:
            start1 = start1.next
            start2 = start2.next
        if start1.data is None and start2.data is None:
            return True
        elif start1.data is None: #and start2.data is not None
            return False
        elif start2.data is None: #and start1.data is not None
            return True
        else:
            if start1.data[0] == start2.data[0]:
                if start1.data[1] > start2.data[1]:
                    if start2.next.data is None:
                        return True
                    return start1.data[0] > start2.next.data[0]
                else:
                    if start1.next.data is None:
                        return False
                    return start1.next.data[0] > start2.data[0]
            return start1.data[0] > start2.data[0]

    def __repr__(self):
        start = self.data.header.next
        rep = ""
        while start.data is not None:
            rep += start.data[0] * start.data[1]
            start = start.next
        return rep



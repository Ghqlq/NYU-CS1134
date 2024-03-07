

#hw 3 q 2

import ctypes  
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iter_collection = None):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1
        if iter_collection is not None:
            for elem in iter_collection:
                self.append(elem)

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def __repr__(self):
        return ("[" + ", ".join("'"+val+"'" if isinstance(val, str) else str(val) for val in self) + "]")

    def __add__(self, other):
        lst  = ArrayList()
        lst  += self 
        lst  += other
        return lst 

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, scalar): 
        lst = ArrayList()
        for i in range(scalar):
            lst.extend(self) 
        return lst

    def __rmul__(self, scalar):
        return self * scalar

    def remove(self, val):
        i = 0
        while i < self.n and self[i] != val:
            i += 1
        while i < self.n - 1:
            self[i] = self[i + 1]
            i += 1
        
        if i < self.n: 
            self[i] = None                                      
            self.n -= 1

    def removeAll(self, val):
        last_val = 0                  
        for i in range(len(self)):  
            if self[i] != val:            
                self[i], self[last_val] = self[last_val], self[i]
                last_val += 1

        while self[i] == val:
           self[i] = None
           i -= 1
           self.n -= 1

    def insert(self, index, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        if not (-self.n <= index <= self.n -1):
            raise IndexError('invalid index')
        if (index < 0):
            index = self.n + index
        self.data[self.n] = self[-1]
        for i in range(self.n-1, index, -1):
            if i>= index:
                self[i] = self[i-1]
        self[index] = val
        self.n += 1
        return self

    def pop(self, index = -1):
        if self.n == 0:
            raise IndexError('This is an empty list')
        if not (-self.n <= index <= self.n -1):
            raise IndexError('invalid index')
        if (index < 0):
            index = self.n + index
        result = self.data[index]
        for i in range(index, self.n - 1):
            self.data[i] = self.data[i+1]
        self.n -= 1
        if self.n < (self.capacity//4):
            self.resize(self.capacity//2)
        return result
      
         


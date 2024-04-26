

#Question 5

from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

def permutations(lst):
    result = []
    stack = ArrayStack()
    q = ArrayQueue()
    for item in lst:
        stack.push(item)
    while stack.is_empty() == False:
        elem = stack.pop()
        if q.is_empty():
            q.enqueue([elem])
        else:
            for i in range(len(q)):
                perm = q.dequeue()
                for j in range(len(perm) + 1):
                    q.enqueue(perm[0:j] + [elem] + perm[j:])
    while q.is_empty() == False:
        result.append(q.dequeue())
    return result

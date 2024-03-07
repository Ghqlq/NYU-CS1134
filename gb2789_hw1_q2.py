
#hw1 Question 2:

def shift(lst, k, direction="left"):
    k = len(lst) - k
    for shift in range(k):
        if direction == "right":
            lst.append(lst.pop(0))
        else:
            lst.insert(0, lst.pop())


#Question 5

def split_parity(lst):
    for i in range(0, len(lst)):
        if lst[i]%2 == 0:
            var = lst[i]
            lst.append(lst.pop(i))
    return lst


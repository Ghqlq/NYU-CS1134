

#q9

def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    new = []
    ranges = high-low +1 
    for i in range(ranges):
        for lsts in permutations(lst, low + 1, high):
            lsts.insert(i, lst[low])
            new.append(lsts)
    return new



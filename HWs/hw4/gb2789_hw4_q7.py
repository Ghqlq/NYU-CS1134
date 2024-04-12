

#q7

def split_by_sign(lst, low, high):
    if low == high:
        return
    elif lst[low] < 0:
        return split_by_sign(lst, low+1, high)
    elif lst[high] > 0:
        return split_by_sign(lst, low, high-1)
    if lst[low] > 0 and lst[high] < 0:
        lst[low], lst[high] = lst[high], lst[low] 
        return split_by_sign(lst, low+1, high-1)
        

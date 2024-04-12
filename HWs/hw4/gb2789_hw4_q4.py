
#q4

def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        other = list_min(lst, low+1, high)
        if lst[low] < other:
            return lst[low]
        return other

lst=[1,2,3,4,5,6,7]
print(list_min(lst, 1, 6))

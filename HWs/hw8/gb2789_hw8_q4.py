
#question 4

from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    lst = [item[0] for item in bst]
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        curr_min = lst[1] - lst[0]
        n = 2
        while n < len(lst):
            curr_min = min(curr_min, lst[n] - lst[n-1])
            n += 1
        return curr_min

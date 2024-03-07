

#question 4

def remove_all(lst, value):
    step = 0
    for i in range(len(lst)):
        if lst[i] == value:
            step += 1
        else:
            lst[i - step] = lst[i]
            
    for i in range(step):
        lst.pop()
    return lst



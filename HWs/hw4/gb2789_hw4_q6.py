

#q6

def appearances(s,low, high):
    if low == high:
        return {s[low]:1}
    dictionary = appearances(s, low+1, high)
    if s[low] not in dictionary:
        dictionary[s[low]] = 1
        return dictionary
    else:
        dictionary[s[low]] += 1
    return dictionary



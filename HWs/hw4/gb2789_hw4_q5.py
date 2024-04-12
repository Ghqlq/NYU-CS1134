

#q5
#a

def count_lowercase(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        return 0
    other = count_lowercase(s, low+1, high)
    return other + count_lowercase(s, low, low)


#b

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low].islower():
            return False
        return True
    return not is_number_of_lowercase_even(s, low, low) ^ is_number_of_lowercase_even(s, low + 1, high)

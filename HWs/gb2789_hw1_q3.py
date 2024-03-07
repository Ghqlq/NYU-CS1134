
#hw1 Question 3:

def sum_of_squares(n):
    result = 0
    while n > 0:
        n-=1
        result += (n**2)
    return result


def sum_of_squares(n):
    return sum(i**2 for i in range(1,n))

#odd

def sum_of_squares_odd(n):
    result = 0
    while n > 0:
        n -= 1
        if n % 2 != 0:
            result += n**2
    return result

def sum_of_squares_odd(n):
    return sum(i**2 for i in range(1, n) if i % 2 != 0)

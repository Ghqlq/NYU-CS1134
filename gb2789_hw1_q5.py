

#hw1 Question 5:
#0 1 1 2 3 5 8 13 21

def fibs(n):
    if n == 0:
        yield
    elif n == 1:
        yield 1
    elif n == 2:
        yield 1
        yield 1
    else:
        a = 1
        b = 1
        yield a
        yield b
        for num in range(n-2):
            a, b = b, a + b
            yield b

    
   
        

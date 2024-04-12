
#Question 1

from ArrayStack import ArrayStack 

def postfix_calculator():
    ops = "+-*/"
    dic = {}
    result = ""
    stack = ArrayStack()
    done = False
    while not done:
        exp = input("--> ")
        if exp == "done()":
            done = True
        else:
            for token in exp.split():
                try:
                    stack.push(int(token))
                except ValueError:
                    if token in dic:
                        stack.push(dic[token])
                    elif token in ops:
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        if token == '+':
                            res = arg1 + arg2
                        elif token == '-':
                            res = arg1 - arg2
                        elif token == '*':
                            res = arg1 * arg2
                        else:
                            if arg2 == 0:
                                raise ZeroDivisionError("No division by 0")
                            res = arg1 / arg2
                        stack.push(res)
                    elif token == "=":
                        result = stack.pop()
                    else:
                        stack.push(token)
        if result != "":
            dic[result] = stack.pop()
            print(result)
            result = ""
        elif not stack.is_empty():
            print(stack.pop())

postfix_calculator()

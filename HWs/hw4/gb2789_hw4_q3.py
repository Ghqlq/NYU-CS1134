
'''
HW 4
'''
#q3
#a

def print_triangle(n):
    if n == 1:
        print("*")
    else:
        print_triangle(n-1)
        print("*"*n)


#b

def print_oposite_triangles(n):
    if n == 1:
        print("*")
        print("*")
    else:
        print("*"*n)
        print_oposite_triangles(n-1)
        print("*"*n)


#c

def print_ruler(n):
    if n == 1:
        print("-")
    else:
        print_ruler(n - 1)
        print("-" * n)
        print_ruler(n - 1)

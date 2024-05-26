
#question 2

from BinarySearchTreeMap import BinarySearchTreeMap

#a)
def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    for i in range(1,n+1):
        tree.insert(i,i)
    return tree

#b)
def add_items(bst, low, high):
    mid = (low+high)//2
    node = bst.insert(mid,mid)
    if low != high:
        add_items(bst, low, mid-1)
        add_items(bst, mid+1, high)

def create_complete_bst(n): 
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

        
        

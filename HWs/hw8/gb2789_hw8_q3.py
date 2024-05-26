#question 3

from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    if prefix_lst is None:
        raise Exception("list is empty")
    else:
        prefix_lst.sort()
        bst = BinarySearchTreeMap()
        for node in prefix_lst:
            bst.insert(node, node)
        return bst


            
    



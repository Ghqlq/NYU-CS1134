
from LinkedBinaryTree import LinkedBinaryTree
#q1

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        current = root.data
        if root.left is None and root.right is None: #leaf node
            return (current, current)
        elif root.right is None:
            left = subtree_min_and_max(root.left)
            return (min(left[0], current),max(left[1], current))
        elif root.left is None:
            right = subtree_min_and_max(root.right)
            return (min(right[0], current),max(right[1], current))
        else:                                     #two children
            left = subtree_min_and_max(root.left)  
            right = subtree_min_and_max(root.right)
            return (min(left[0], right[0], current), max(left[1], right[1], current))
    if bin_tree.root is None:  
        raise Exception("Tree is empty")
    return subtree_min_and_max(bin_tree.root)

    

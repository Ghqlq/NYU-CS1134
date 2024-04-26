
from LinkedBinaryTree import LinkedBinaryTree

#q3

def is_height_balanced(bin_tree):
    def subtree_height_balanced(root):
        if root is None:
            return (True, 0)
        left = subtree_height_balanced(root.left)
        right = subtree_height_balanced(root.right)
        balance = max(left[1], right[1])+1
        if (left[0] and right[0]) and abs(left[1]-right[1])<=1:
            return (True, balance)
        return (False, balance)
    if bin_tree.root is None:
        raise Exception("Tree is empty")
    return subtree_height_balanced(bin_tree.root)[0]
    
        
        

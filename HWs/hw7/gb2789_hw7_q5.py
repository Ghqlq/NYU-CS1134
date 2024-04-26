
from LinkedBinaryTree import LinkedBinaryTree

#q5

def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split(" ")
    pointer = None
    for exp in prefix_exp:
        if pointer is None:
            pointer = LinkedBinaryTree.Node(exp)
            tree = LinkedBinaryTree(pointer) 
        elif pointer.left is None:
            if exp.isnumeric():
                pointer.left = LinkedBinaryTree.Node(int(exp))
                pointer.left.parent = pointer
            else:
                pointer.left = LinkedBinaryTree.Node(exp)
                pointer.left.parent = pointer
                pointer = pointer.left
        elif pointer.right is None:
            if exp.isnumeric():
                pointer.right = LinkedBinaryTree.Node(int(exp))
                pointer.right.parent = pointer
            else:
                pointer.right = LinkedBinaryTree.Node(exp)
                pointer.right.parent = pointer
                pointer = pointer.right
        else: #left and right are not None
            while pointer.right is not None:
                pointer = pointer.parent
            if exp.isnumeric():
                pointer.right = LinkedBinaryTree.Node(int(exp))
                pointer.right.parent = pointer
            else:
                pointer.right = LinkedBinaryTree.Node(exp)
                pointer.right.parent = pointer
                pointer = pointer.right
    res = LinkedBinaryTree(tree.root)
    return res
        

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    ordered = " ".join(str(node.data) for node in tree.postorder())
    return ordered


 

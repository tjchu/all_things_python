# A utility class that represents an individual node in a Binary Search Tree
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 




"""
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
"""


# Binary Search Tree Find with the give value to search for
def search(root,key): 
	
	# Base Cases: root is null or key is present at root 
	if root is None or root.val == key: 
		return root 

	# Key is greater than root's key 
	if root.val < key: 
		return search(root.right,key) 
	
	# Key is smaller than root's key 
	return search(root.left,key) 


# A utility function to insert a new node with the given key 
def insert(root,node): 
	if root is None: 
		root = node 
	else: 
		if root.val < node.val: 
			if root.right is None: 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if root.left is None: 
				root.left = node 
			else: 
				insert(root.left, node) 




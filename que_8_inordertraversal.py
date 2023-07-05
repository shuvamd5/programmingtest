class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def inorder(root):

	if root:
		# First recur on left child
		inorder(root.left)
		# Then print the data of node
		print(root.val, end=" "),
		# Now recur on right child
		inorder(root.right)


# start
def st():
	root = Node(input("Enter the root node : "))
	root.left = Node(input("Enter left child of root : "))
	root.right = Node(input("Enter right child of root : "))
	root.left.left = Node(input("Enter left child of left child : "))
	root.left.right = Node(input("Enter right child of left child : "))

	# Function call
	print("Inorder traversal of binary tree is : ")
	inorder(root)


st()

class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None
		self.data  = data

class BSTree:
	def __init__(self):
		self.root = None
	
	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
			return self.root
		if data < self.root.data:
			if self.root.left is None:
				self.root.left = Node(data)
			else:
				self.root.left = self.insert(data)
		else:
			if self.root.right is None:
				self.root.right = Node(data)
			else:
				self.root.right = self.insert(data)
		return self.root

	def show(self, node):
		if node is None:
			return
		
		if node.left:
			self.show(node.left)
		print node.data
		if node.right:
			self.show(node.right)


bst = BSTree()
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.show(bst.root)

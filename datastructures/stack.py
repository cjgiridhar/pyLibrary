class Stack:
	""" 
	Stack implementation in Python
	"""
	def __init__(self):
		self.stack = []

	def push(self, item):
		"""
		Push an item in stack
		"""
		self.stack.insert(0,item)
	
	def pop(self):
		"""
		Pop an item from stack
		"""
		return self.stack.pop(0)

	def show(self):
		"""
		Show complete stack
		"""
		return self.stack

	def top_of_stack(self):
		"""
		Returns top of stack
		"""
		return self.stack[0]

if __name__ == '__main__':
	stack = Stack()
	stack.push(3)
	stack.push(4)
	print stack.show()
	stack.push(33)
	stack.push(444)
	print "Show Stack: ", stack.show()
	print "Top: ", stack.top_of_stack()
	stack.pop()
	print "Show Stack: ",stack.show()

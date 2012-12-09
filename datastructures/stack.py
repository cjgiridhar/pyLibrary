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
		self.stack.append(item)
	
	def pop(self):
		"""
		Pop an item from stack
		"""
		popped = self.stack[-1]
		del self.stack[-1]
		return popped

	def show(self):
		"""
		Show complete stack
		"""
		return self.stack

	def top_of_stack(self):
		"""
		Returns top of stack
		"""
		return self.stack[-1]

if __name__ == '__main()__':
	stack = Stack()
	stack.push(3)
	stack.push(4)
	print stack.show()
	stack.push(33)
	stack.push(444)
	print stack.show()
	print stack.top_of_stack()
	stack.pop()
	print stack.show()

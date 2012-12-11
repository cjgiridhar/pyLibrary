class Queue:
	"""
		Queue implementation in Python
	"""

	def __init__(self,size):
		"""
			Size of the queue is fixed
		"""
		self.queue = []
		self.SIZE = size
		
	def __isEmpty(self):
		"""
			Provate method to check if queue is empty
		"""
		if len(self.queue) == 0:
			raise Exception, "Queue is empty!!"
			
	def __isFull(self):
		"""
			Private method to check if queue is full
		"""
		if len(self.queue) == self.SIZE:
			raise Exception, "Queue is full!!"
			
	def enqueue(self, item):
		"""
			Inserts an element in queue
		"""
		self.__isFull()
		return self.queue.insert(0,item)
		
	def dequeue(self):
		"""
			Removes an element from queue
		"""
		self.__isEmpty()
		return self.queue.pop()

	def show(self):
		return self.queue

if __name__ == '__main__':		
	Q = Queue(10)
	Q.enqueue(3)
	Q.enqueue(4)
	print Q.show()
	Q.dequeue()
	print Q.show()
		

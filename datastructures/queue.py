class Queue:
	def __init__(self,size):
		self.queue = []
		self.SIZE = size
		
	def isEmpty(self):
		if len(self.queue) == 0:
			print "Queue is empty!!"
			exit(1)
		else:
			print "Queue contains elements!!"
			exit(1)
			
	def isFull(self):
		if len(self.queue) == self.SIZE:
			print "Queue is full!!"
			exit(1)
			
	def enqueue(self, item):
			self.isFull()
			self.queue.append(item)
			return self.queue
		
	def dequeue(self):
		self.isEmpty()
		temp = self.queue[0]
		del self.queue[0]
		return temp

	def show(self):
		print self.queue

if __name__ == '__main__':		
	Q = Queue(10)
	Q.isEmpty()
	Q.enqueue(3)
	Q.enqueue(4)
	Q.show()
	Q.dequeue()
	Q.dequeue()
	Q.dequeue()
	Q.show()
		

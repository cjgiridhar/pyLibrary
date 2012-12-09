class PriorityQueue:
	def __init__(self):
		self.queue = {}
		self.priByData = {}
		self.priKey = None
		self.data = None

	def show(self):
		return self.queue
		
	def add(self, data, priority):
		self.data = data
		self.priority = priority

		if self.data in self.priByData.keys():
			raise Exception, "%d exists in queue" %self.data
		else:
			self.priByData[self.data] = self.priority
		
		if self.priority in self.queue.keys():
			raise Exception, "%d exists in queue" %self.priority
		else:
			self.queue[self.priority] = self.data
		
		self.priKey = min(self.queue.keys())
			
	def delete(self, data):
		self.data = data
		if self.data not in self.priByData.keys():
			raise Exception, "%d doesn't exist in queue" %self.data
		else:
			self.priByData.pop(self.data)
			
		flag = 0
		for keys in self.queue.keys():
			if self.queue[keys] == self.data:
				self.queue.pop(keys)
				return
			else:
				flag = 1
				
		if flag:
			raise
			
	def modify(self,data,priority):
		self.data = data
		self.priority = priority
		if self.data not in self.priByData.keys():
			raise Exception, "%d doesn't exist in queue" %self.data
		else:
			self.priByData[self.data] = self.priority
		
		flag = 0
		for keys in self.queue.keys():
			if self.queue[keys] == self.data:
				self.queue.pop(keys)
				self.queue[self.priority] = self.data
				return
			else:
				flag = 1
				
		if flag:
			raise
		
if __name__ == '__main()__':
	queue = PriorityQueue()
	queue.add(15,1)
	queue.add(13,2)
	queue.add(11,3)
	print queue.show()
	queue.delete(11)
	print queue.show()
	queue.modify(15,5)
	print queue.show()

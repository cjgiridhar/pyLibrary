class Node:
	def __init__(self, data=None, next=None):
		self.next = next
		self.data = data


class List:
	def __init__(self):
		self.first = None
		self.last = Node(None,None)

	def insert(self,data):
		if self.first is None:
			self.first = Node()
			self.first.next = self.last
			self.first.data = data
		else:
			temp = self.first
			while temp.next != self.last:
				temp = temp.next
			temp.next = Node()
			temp.next.next = self.last
			temp.next.data = data
		return self.first	

	def insert_at_start(self,data):
		temp = self.first
		self.first = Node()
		self.first.next = temp
		self.first.data = data

	def show(self):
		temp = self.first
		while temp != self.last:
			print temp.data
			temp = temp.next
		print self.last.data			
	
	def delete(self, data):
		temp = self.first
		while temp != self.last:
			if temp.next.data == data:
				temp.next = temp.next.next
				break
		return self.first

list = List()
list.insert(6)
list.insert(5)
list.delete(5)
list.insert_at_start(3)
list.show()
			

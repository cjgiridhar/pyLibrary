class Node:
	def __init__(self, item=None, next=None):
		self.item = item
		self.next = next
		
def add(head, item):
	if head.next is None:
		head.item = item
		head.next = head
	else:
		temp = head
		while temp.next is not head:
			temp = temp.next
		temp.next = Node()
		temp = temp.next
		temp.item = item
		temp.next = head
	return head

def destroy(head, item):
	current = head
	while True:
		current = current.next
		if current.next.item == item:
			current.next = current.next.next
			break
	return head
	
def showList(head):
	current = head
	while True:
		print current.item
		current = current.next
		if current is head:
			break

node = Node()
node = add(node, 3)
node = add(node, 4)
node = add(node, 44)
node = add(node, 45)
showList(node)
node = destroy(node, 44)
showList(node)

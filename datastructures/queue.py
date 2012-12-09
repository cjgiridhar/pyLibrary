#############################################################################
# Queue.py - Implementation of Queue in Python
# 1. enqueue - Adds an item to the queue
# 2. dequeue - Remove an element from queue
# 3. show - Lists the contents of queue
# 4. isEmpty - To check if queue is empty
# 5. isFull - To check if queue is full
#
# PyLibrary                      Version 1.0
# Copyright 2010 Chetan Giridhar cjgiridhar@gmail.com
# Created: 04/15/2012             Last Modified: 04/15/2012
#
# This file is part of PyLibrary.
#
# PyLibrary is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 as published by
# the Free Software Foundation; 
#
# PyLibrary is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#                                                                             
#############################################################################
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
		
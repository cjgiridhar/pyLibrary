#############################################################################
# Stack.py - Implementation of stack in Python
# 1. push - Add an item to stack
# 2. pop - Remove an element from stack
# 3. top_pf_stack - Returns item at the top of stack
# 4. show - Lists the contents of stack
#
# PyLibrary                      Version 1.0
# Copyright 2010 Chetan Giridhar cjgiridhar@gmail.com
# Created: 04/14/2012             Last Modified: 04/14/2012
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

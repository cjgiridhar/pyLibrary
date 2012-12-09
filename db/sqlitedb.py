#############################################################################
# SQLiteHandler.py - Class is responsible for working with the SQlite databases.
#
# PyLibrary                      Version 1.0
# Copyright 2010 Chetan Giridhar cjgiridhar@gmail.com
# Created: 11/15/2010             Last Modified: 11/16/2010
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


import sqlite3

class SQLiteHandler:
	"""
		SQLiteHandler class is responsible for working with the SQlite databases.
		
		__init__() - Takes the path of the database as an argument. 
		connect() - Establishes a connection to the database.
		execute() - Executes the SQL queries on the database.
		commit() - This method commits the current transaction.
		close() - This closes the database connection.
	"""
	
	def __init__(self, _databasepath):
		self.path = _databasepath 
		self.connection = None
		self.cusrsorobj = None
		self.query = None
		
	def connect(self):
		try:
			self.connection = sqlite3.connect(self.path)
			self.cursorobj = self.connection.cursor()			
		except Exception: 
			print "Error connecting to the Database!"
	
	def execute(self,query):
		self.query = query
		try:
			if self.cursorobj is not None:
				self.cursorobj.execute(self.query)
				return self.cursorobj
		except Exception:
			print "Query execution failed!"	
		
	def commit(self):
		try:
			if self.connection is not None:
				self.connection.commit()
		except Exception:
			print "Error commiting query!"
	
	def close(self):
		try:
			if self.cursorobj is not None:
				self.cursorobj.close()
		except Exception:
			print "Error while closing the connection!"

if __name__ == '__main()__':
	sql = SQLiteHandler('C:\\db')


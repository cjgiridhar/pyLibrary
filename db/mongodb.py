import pymongo
from pymongo import Connection

class MongoHandler:
	"""
		MongoHandler class is responsible for working with the Mongo databases.
		
		__init__() - Takes the path of the database as an argument. 
		connect() - Establishes a connection to the database.
		execute() - Executes the mongodb queries on the database.
		commit()  - Commands on mongodb get commited implicitly.
		close()   - Database connection gets closed implicitly.

	"""

	def __init__(self, _databasename, _server, _port):
		self.databasename = _databasename 
		self.server = _server
		self.port = _port
		self.connectionObj = None
		self.dbObj = None
		self.collectionObj = None
		self.query = None
		
	def connect(self):
		try:
			self.connection = Connection(self.server, self.port)	
			self.db = self.connection[self.databasename]
			return self.db
		except Exception: 
			print "Error connecting to the Database!"

	def execute(self,query):
		self.query = query
		try:
			if self.db is not None:
				self.cursorObj = eval('self.db' + "." + self.query)
				return self.cursorObj
		except Exception:
			print "Error executing the query!!"	
			
	def commit(self):
		pass
		
	def close(self):
		pass

if __name__ == '__main()__':		
	mongo = MongoHandler('mydb','localhost', 27017)
	dbObj = mongo.connect()

	import datetime
	post = {"author": "Mike",
			"text": "My first blog post!",
			"tags": ["mongodb", "python", "pymongo"],
			"date": datetime.datetime.utcnow()}
	print mongo.execute('posts.insert(post)')
	print mongo.execute('posts.find()')

	mongo.commit()
	mongo.close()

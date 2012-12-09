class Convertor:
	def __init__(self,  records, separator):
		self.records = records
		self.separator = separator
		self.dict = {}
		
	def convertToColumns(self):
		for lines in self.records:
			length = len(str(lines).split(self.separator))
			pass
		for iterator in range(length):
			self.dict[iterator] = []
		for lines in self.records:
			if type(lines) is str:
				elements = lines.split(self.separator)
				for iterator in range(length):
					self.dict[iterator].append(elements[iterator]) 
			if	type(lines) is tuple:
				for iterator in range(length):
					self.dict[iterator].append(lines[iterator])
		return self.dict

if __name__ == '__main__':

## UseCase: Read records from CSV file and convert to columns
	fileHandle = open('C:\\Python25\\input.csv', 'r')
	convert = Convertor(fileHandle.readlines() , ',')
	fileHandle.close()
	dict = convert.convertToColumns()
	print "First column in file records ", dict[0]
	

## UseCase: Read records from a SQLite database
	from SQLiteHandler import SQLiteHandler
	sql = SQLiteHandler('C:\\db')
	sql.connect()
	rows = sql.execute(" select * from data")
	sql.commit()
	sql.close()
	convert = Convertor(rows.fetchall(), ',')
	dict = convert.convertToColumns()
	print "First column in DB records ", dict[0]
	


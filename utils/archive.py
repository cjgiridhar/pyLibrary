import zlib

class Archive:
	""" 
	Acrchive class to support compression formats.
	
	__init__() - Takes the following as arguments.
		Filepath or string to be arhived
		
	- zlib() - Compress and decompress file or string in zlib format.
	
	"""
	
	def __init__(self, filepath = None, string = None):
		self.filepath = filepath
		self.string = string

		if self.filepath and self.string is None:
			raise "Either a string or a filepath should be present"
			
		if self.string is not None:
			self.isString = True			
			try:
				if type(self.string) is str:
					pass
			except Exception,msg:
				raise
		if self.filepath is not None:
			self.isFile = True
			try:
				self.fileobj = file(self.filepath, 'rb')
			except Exception,msg:
				raise
				
	def __encodedString(self, hash):
		return hash.hexdigest()

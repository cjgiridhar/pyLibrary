import httplib2


class Rest:
	"""
		Rest.py - Class responsible for sending GET/POST/PUT and DELETE requests.
		get() - sends get requests to the URL.
		post() - send post data to the URL.
		put() - sends PUT requests
		delete() - sends DELETE requests
	"""
	
	def __init__(self):
		self.url = None
		self.handler = httplib2.Http(".cache")

	def get(self, url):
		self.url = url
		try:
			resp, content = self.handler.request(self.url, "GET")
			
		except Exception:
			raise Exception("Exception while connecting to %s" %self.url)
			exit(1)
		
		return (resp, content)
		

if __name__ == '__main()__':
	rest = Rest()
	rest.get('http://google.com')

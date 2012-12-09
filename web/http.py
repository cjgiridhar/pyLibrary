import urllib
import urllib2
import string 

class Http:
	"""
		http.py - Class responsible for sending GET and POST requests.
		get() - sends get requests to the URL.
		post() - send post data to the URL.
	"""
	
	def __init__(self):
		self.url = None
		self.server = None

	def get(self, url):
		self.url = url
		request = urllib2.Request(self.url)
		try:
			get_response = urllib2.urlopen(request)
		except Exception:
			raise Exception("Exception while connecting to %s" %self.url)
			exit(1)
				
		response = get_response.read()
		return response
		

	def post(self, url, values):
		self.url = url
		self.values = values
		data =  urllib.urlencode(self.values)
		request = urllib2.Request(self.url, data)
		try:
			get_response = urllib2.urlopen(request)
		except Exception:
			raise Exception("Exception while connecting to %s" %self.url)
			exit(1)
		
		response = get_response.read()
		return response	

if __name__ == '__main()__':
	httpreq = Http()
	print httpreq.get('www.google.com')
	values = {}
	values = {'name':'Chetan Giridhar'}
	print httpreq.post('http://www.rediff.com', values)

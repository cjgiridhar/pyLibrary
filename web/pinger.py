
class Pinger:
	def __init__(self):
		self.dictOfUrls = {}
		self.link = {}
		self.http = httplib2.Http() 

	def pingPage(self, url):
		"""
		Pinging links on a web page 
		"""
		status, response = self.http.request(url)
		for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
	    		if link.has_key('href'):
				if re.match('http',str(link['href'])):
					if not self.dictOfUrls.has_key(str(link['href'])):
						try:
        						status, response = self.http.request(str(link['href']))
							self.dictOfUrls[str(link['href'])] = status['status']
						except:
							self.dictOfUrls[str(link['href'])] = 'Could not connect'
							continue
					else:
						continue

				else:
					continue
		return self.dictOfUrls

	def pingLink(self, url):
		"""
		Pinging given link
		"""
		try:
			status, response = self.http.request(url)
			self.link[url] = status['status']
		except:
			self.link[url] = 'Could not connect'
		return self.link

		
if __name__ == '__main()__':
	ping = Pinger()
	print ping.pingPage('http://www.technobeans.wordpress.com/talk')
	print ping.pingLink('http://www.technobeans.wordpress.com/talk')
 

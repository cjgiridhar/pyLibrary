import wmi
import os
import time
import string

__DELAY = 20

class Service:
	""" 
     1. The Service Class is aimed at starting and stopping the services based on the service name given as an input.
     2. __init__() - gets the name of the service
     3. getstatus() - gets the status of the services - Running or Stopped.
     4. start(),stop() - would start and stop the services respectively by first getting the status of the service. 
     5. If the service is already started/stopped, it will print a message that the service is already running/stopped.
	 6. start() and stop() functions work in 2 modes: Using DOS command SC and using Windows Management Instrumentation. Default mode being "SC".
	"""
 
	def __init__(self, service):
		self.wmiObj = wmi.WMI()
		self.service = service
	
	
	def getstatus(self):
		return self.wmiObj.Win32_Service(Name=self.service)[0].State
	
	def start(self, mode="sc"):
		if mode.upper() == "SC":
			try:
				if(self.getstatus() == "Running"):
					raise Exception("%s service is already running " % self.service)
				else:
					command = 'sc.exe start ' + self.service 
					os.system(command)
					time.sleep(__DELAY)
			except Exception:
				raise	
		if mode.upper() == "WMI":
			try:
				if self.getstatus()=="Running":
					raise Exception("%s service is already running " % self.service)
				else: 
					self.wmiObj.Win32_Service(Name=self.service)[0].StartService()
					time.sleep(__DELAY)
			except Exception:
				raise

				
	
	def stop(self, mode="sc"):
		if mode.upper() == "SC":
			try:
				if(self.getstatus() == "Stopped"):
					raise Exception("%s service is already stopped " % self.service)
				else:
					command = 'sc.exe stop ' + self.service 
					os.system(command)
					time.sleep(__DELAY)
			except Exception:
				raise
		if mode.upper() == "WMI":
			try:
				if self.getstatus()=="Stopped":
					raise Exception("%s service is already stopped " % self.service)
				else: 
					self.wmiObj.Win32_Service(Name=self.service)[0].StopService()
					time.sleep(__DELAY)
			except Exception:
				raise 	



	

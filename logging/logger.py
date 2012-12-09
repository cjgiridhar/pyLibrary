import os

class Log:
    def __init__(self, debugMode=0):
		self.bDebug = debugMode
		self.reportLog = None
		self.errorLog = None 
		self.infoLog = None
        
    def stdout (self, msg):
        print msg
        if self.bDebug:
            self.info(msg + "\n")      

    def results (self, msg):
        self.reportLog.write(msg + "\n")
        self.reportLog.flush()
        if self.bDebug:
            self.info(msg + "\n")
            
    def error (self, msg):
        self.errorLog.write(msg + "\n")   
        self.errorLog.flush()        
        if self.bDebug:
            self.info(msg + "\n")

    def info (self, msg):
		if self.bDebug:
			self.infoLog.write(msg + "\n")        
			self.infoLog.flush()
            
    def setDebugMode(self, mode):
        print "Debug mode", mode
        self.bDebug = mode
        
    def setReportPath(self, path, mode="w"):
        self.reportLog = open(path, mode)

    def setInfoPath(self, path):
        self.infoLog = open(path, "a")

    def setErrorPath(self, path):
		import os
		self.errorLog = open(path, "a")
        
    def stop(self):
        if self.reportLog:
            self.reportLog.close()
        if self.errorLog:
            self.errorLog.close()
        if self.infoLog:
            self.infoLog.close()

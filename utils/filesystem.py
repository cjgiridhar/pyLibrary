import shutil
import os
import sys
import time
import cPickle

class FileSystem:
	def copyDir(self,src, dest):
		try:
			shutil.copytree(src, dest) 
		except Exception, msg:
			return msg


	def copyFile (self,src, dest):
		try:
			shutil.copyfile(src, dest)
		except Exception, msg:
			return msg


	def createDirPath(self,path):
		try:
			if not os.path.isdir(path):
				os.makedirs(path)
		except Exception, msg:
			return msg


	def removeDir(self,path):
		try:
			if os.path.isdir(path):
				shutil.rmtree(path)
		except Exception, msg:
			return msg


	def removeFile(self,path):
		if os.path.exists(path):
				os.remove(path)

	def touchFile(self,filepath):
		if not os.path.exists(filepath):
			f = open(filepath,"w")
			f.close()
			return 1
		elif os.stat(filepath)[6] < 5L:
			return 1
		else:
			return 0

	def renameFile(self, src, dest):
		try:
			if not os.path.exists(src):
					print False
		except Exception, msg:
			return msg
		try:	
			if os.path.isfile(src):
				shutil.move(src,dest)
		except Exception, msg:
			return msg
		
	def isFile(self,fPath):
        	try:
				fStatus = os.path.isfile(fPath)
				return fStatus
        	except:
				return "Object type could not be determined"
		
	def isDir(self,dirPath):
		try:
			dStatus = os.path.isdir(dirPath)
			return dStatus
		except:
			return"Object type could not be determined"
		
	def pathExists(self,fsPath):
		try:
			fsStatus = os.path.exists(fsPath)
			return fsStatus
		except:
			return "Object's existence could not be determined"
			
if __name__ == '__main__':
	fs = FileSystem()
	print fs.pathExists('C:\\Python25\\input.csv')
	fs.touchFile('C:\\touch.txt')
	fs.renameFile('C:\\restrict.txt','restr.txt') ## Moves the file as dest is not in same dir path
	fs.renameFile('C:\\vol.txt', 'C:\\vol1.txt')  ## Renames the file as dest is in same dir path
	print fs.isDir('C:\\pyutf')		
	fs.createDirPath("C:\\test\\test")
	



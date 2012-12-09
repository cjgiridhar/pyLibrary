import os
import time, sys

class VirtualMCHandler:
	"""
	VirtualMCHandler class helps in managing Virtual Machines.
	It has 4 functions that perform various operations on a VM.
	__init__() - Takes the path of the Virtual Machine as its argument.
	start() - Starts the  Virtual Machine Image.
	stop() - Stops the  Virtual Machine Image.
	takesnapshot(snapshotname) - Takes the Snaphot of  Virtual Machine Image. Argument is the new snapshot name.
	revertsnapshot(snapshotname) - Reverts the Virtual Machine Image to the previously taken snaphot name as mentioned in its argument.
	"""

	def __init__(self, VMPath):
		self.path = "\"" + VMPath + "\""
		if not os.path.exists(self.path):
			print "Please check the path of .vmx %s" %self.path
			sys.exit(0)
		
	def start(self):
		_vmstart = "vmrun.exe -T ws start " + self.path + ""
		os.system(_vmstart)

	def stop(self):
		_vmstop = "vmrun.exe -T ws stop " + self.path + ""
	    	os.system(_vmstop)

	def takesnapshot(self,snapshotname):
		self.snapshotname = "\"" + snapshotname + "\""
		_vmsnapshotname = "vmrun.exe -T ws snapshot " + self.path + " " + self.snapshotname
		os.system(_vmsnapshotname)
	
	def revertsnapshot(self,snapshotname):
		self.snapshotname = "\"" + snapshotname + "\""
		_vmrevert = "vmrun.exe -T ws revertToSnapshot " + self.path + " " + self.snapshotname
		os.system(_vmrevert)

if __name__ == '__main__':
	vm = VirtualMCHandler("ARG")
	vm.start()
	vm.takesnapshot("ARG")
	vm.revertsnapshot("ARG")
	vm.stop()

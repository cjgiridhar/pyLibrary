import _winreg
import re
import os
import subprocess


"""
	Module implementing registry utility functions
"""

_regMap = { "HKLM" : _winreg.HKEY_LOCAL_MACHINE,
			"HKCR" : _winreg.HKEY_CLASSES_ROOT,
			"HKCU" : _winreg.HKEY_CURRENT_USER,
			"HKU"  : _winreg.HKEY_USERS,
			"HKCC" : _winreg.HKEY_CURRENT_CONFIG
		}

_regValType = { 1 : _winreg.REG_SZ,
				2 : _winreg.REG_EXPAND_SZ,
				3 : _winreg.REG_BINARY,
				4 : _winreg.REG_DWORD,
				7 : _winreg.REG_MULTI_SZ
			}

REG_SZ =			_winreg.REG_SZ
REG_EXPAND_SZ =		_winreg.REG_EXPAND_SZ
REG_BINARY =		_winreg.REG_BINARY
REG_DWORD =			_winreg.REG_DWORD
REG_MULTI_SZ =		_winreg.REG_MULTI_SZ

def _splitParts(regKey):
	"""
		Split registry hive name from rest of a key name. Return both.
	"""
	regParts = re.search(r"^(.+?)\\(.+)$", regKey)
	regHive = _regMap[regParts.group(1).upper()]
	subKey = regParts.group(2)
	return (regHive, subKey)


def createKey(regKey):
	"""
		Method to create a registry key

		@type regKey: string
		param regVal: Registry key to create.
	"""
	try:
		(regHive, subKey) = _splitParts(regKey)
		_winreg.CreateKey(regHive, subKey)
	except:
		raise Exception ("Registry entry %s could not be added" % regKey)


def setValue(regKey, regValName, regVal, regType=1):
	"""
		Method to create a registry value

		@type regKey: string
		param regKey: Registry key to be added.

		@type regValName: string
		param regValName: Name of registry value.

		@type regVal: string
		param regVal: Registry value data.

		@type regType: string
		param regType: Registry type: 1 - REG_SZ, 2 - REG_EXPAND_SZ, 3 - REG_BINARY, 4 - REG_DWORD, 7 : REG_MULTI_SZ
	"""
	try:
		(regHive, subKey) = _splitParts(regKey)
		regValueType = _regValType[regType]

		try:
			hkey = _winreg.OpenKey(regHive, subKey, 0, _winreg.KEY_WRITE)
		except Exception, msg:
			raise Exception("Unable to open Registry key : %s" % regKey)
		else:
			_winreg.SetValueEx(hkey, regValName, 0, regValueType, regVal)
			_winreg.CloseKey(hkey)
	except:
		raise Exception ("Registry value %s with value data %s of type %s could not be added to %s" % (regValName, regVal, regValueType, regKey))


def delValue(regKey, regValName):
	"""
		Method to delete a registry value

		@type regKey: string
		param regKey: Registry key.

		@type regValName: string
		param regValName: Registry value to be deleted.
	"""
	try:
		(regHive, subKey) = _splitParts(regKey)

		try:
			hkey=_winreg.OpenKey(regHive, subKey, 0, _winreg.KEY_ALL_ACCESS)
		except Exception, msg:
			raise Exception("Unable to open Registry key : %s" % regKey)
		else:
			_winreg.DeleteValue(hkey, regValName)
			_winreg.CloseKey(hkey)
	except:
		raise Exception ("Registry value %s could not be deleted from %s" % (regValName, regKey))


def delKey(regKey):
	"""
		Method to delete a registry key

		@type regKey: string
		param regKey: Registry key to be deleted.
	"""
	try:
		(regHive, fullSubKey) = _splitParts(regKey)

		subKeyParts = re.search(r"^(.+)\\(.+)$", fullSubKey)
		subKey = subKeyParts.group(1)
		dKey = subKeyParts.group(2)

		try:
			hkey=_winreg.OpenKey(regHive, subKey, 0, _winreg.KEY_ALL_ACCESS)
		except Exception, msg:
			raise Exception("Unable to open Registry key : %s" % regKey)
		else:
			_winreg.DeleteKey(hkey, dKey)
			_winreg.CloseKey(hkey)
	except:
		raise Exception ("Registry key %s could not be deleted" % regKey)


def delKeyTree(regKey):
	"""
		Method to delete a registry tree

		@type regKey: string
		param regKey: Registry key to be deleted with all subkeys and values.
	"""
	cmdArgs = [ "reg", "delete", regKey, "/f" ]

	proc = subprocess.Popen(cmdArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	STDOUT, STDERR = proc.communicate()
	returnCode = proc.returncode

	if returnCode != 0 :
		raise Exception("Failed to delete registry tree %s. Error %d\n%s\n%s" % (regKey, returnCode, STDOUT, STDERR))


def keyExists(regKey):
	"""
		Method to check if a registry key exists

		@type regKey: string
		param regKey: Registry key.

		@rtype:	  bool
		@return:  True - key exists, False - Key doesn't exists
	"""

	result = False

	try:
		(regHive, subKey) = _splitParts(regKey)

		try:
			hkey=_winreg.OpenKey(regHive, subKey, 0, _winreg.KEY_READ)
		except:
			pass
		else:
			_winreg.CloseKey(hkey)
			result = True
	except:
		pass

	return result


def valExists(regKey, regVal):
	"""
		Method to check if a registry value exists

		@type regKey: string
		param regKey: Registry key.

		@type regVal: string
		param regVal: Registry Value Name.

		@rtype:	  bool
		@return:  True - Value exists, False - Value doesn't exists
	"""

	result = False

	try:
		(regHive, subKey) = _splitParts(regKey)

		try:
			hkey=_winreg.OpenKey(regHive, subKey, 0, _winreg.KEY_READ)
		except:
			pass
		else:
			try:
				valinfo = _winreg.QueryValueEx(hkey, regVal)
			except:
				pass
			else:
				result = True

			_winreg.CloseKey(hkey)
	except:
		pass

	return result


def getValue(regKey, regValName):
	"""
		Method to get a registry value

		@type regKey: string
		param regKey: Registry key.

		@type regValName: string
		param regValName: Registry Value Name.

		@rtype: list
		@return: List containing value data and type. Value data will be a unicode string and registry type: Registry type: 1 - REG_SZ, 2 - REG_EXPAND_SZ, 3 - REG_BINARY, 4 - REG_DWORD, 7 : REG_MULTI_SZ
	"""

	result = None

	try:
		(regHive, subKey) = _splitParts(regKey)

		try:
			hkey=_winreg.OpenKey(regHive, subKey, 0, _winreg.KEY_READ)
		except Exception, msg:
			raise Exception("Unable to open Registry key : %s" % regKey)
		else:
			try:
				result = _winreg.QueryValueEx(hkey, regValName)
			except Exception, msg:
				raise Exception("Unable to open Registry value : %s %s" % (regKey, regValName))

			_winreg.CloseKey(hkey)
	except:
		print "Registry value %s under the key %s could not be fetched" % (regValName, regKey)

	return result


def getAllValues(regKey):
	"""
		Method to get all values under a registry key

		@type regKey: string
		param regKey: Registry key.

		@rtype:	  list
		@return:  List containing value name,value data and type. Value data will be a unicode string and registry type: Registry type: 1 - REG_SZ, 2 - REG_EXPAND_SZ, 3 - REG_BINARY, 4 - REG_DWORD, 7 : REG_MULTI_SZ
	"""

	result = []

	try:
		(regHive, subKey) = _splitParts(regKey)

		try:
			hkey=_winreg.OpenKey(regHive,subKey,0,_winreg.KEY_READ)
		except Exception, msg:
			raise Exception("Unable to open Registry key : %s" % regKey)
		else:
			numvals=_winreg.QueryInfoKey(hkey)
			for indVals in range(0, numvals[1]):
				result.append(_winreg.EnumValue(hkey, indVals))
			_winreg.CloseKey(hkey)
	except:
		print "Registry values under the key %s could not be fetched" % regKey

	return result


def saveKey(regKey, filename):
	"""
		Save a named registry key to soecified file. If the file exists it will be overwritten

		@type regKey: string
		param regKey: Registry key.

		@type filename: string
		param filaname: name of file in which to save tree.
	"""

	# Post Win XP the "reg" command has a "/y" option to force overwriting an existing file... this
	# does not exist on XP so we first have to make sure that there is no existing saved file.

	if os.path.exists(filename):
		os.remove(filename)

	cmdArgs = [ "reg", "export", regKey, filename ]

	proc = subprocess.Popen(cmdArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	STDOUT, STDERR = proc.communicate()
	returnCode = proc.returncode

	if returnCode != 0 :
		raise Exception("Failed to save registry key %s. Error %d\n%s\n%s" % (regKey, returnCode, STDOUT, STDERR))

	return


def loadKey(filename):
	"""
		Load a registry key from the specified file

		@type filename: string
		param filaname: name of file containing registry tree to restore.
	"""
	cmdArgs = [ "reg", "import", filename ]

	proc = subprocess.Popen(cmdArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	STDOUT, STDERR = proc.communicate()
	returnCode = proc.returncode

	if returnCode != 0 :
		raise Exception("Failed to restore registry key from file %s. Error %d\n%s\n%s" % (filename, returnCode, STDOUT, STDERR))

	return


#---------------------------End of Module------------------------------------

if __name__ =="__main__":

	createKey(r"HKCU\Software\AGM\test")
	setValue(r"HKCU\Software\AGM\test", "stringValue", "42", 1)
	setValue(r"HKCU\Software\AGM\test", "numberValue", 42, 4)
	delValue(r"HKCU\Software\AGM\test", "numberValue")
	delKey(r"HKCU\Software\AGM\test")
	createKey(r"HKCU\Software\AGM\test2")
	setValue(r"HKCU\Software\AGM\test2", "stringValue", "42", 1)
	createKey(r"HKCU\Software\AGM\test2\level1")
	setValue(r"HKCU\Software\AGM\test2\level1", "numberValue", 42, 4)
	saveKey(r"HKCU\Software\AGM\test2", "test.reg")
	delKeyTree(r"HKCU\Software\AGM\test2")
	print keyExists(r"HKCU\Software\AGM\test2")
	loadKey("test.reg")
	print keyExists(r"HKCU\Software\AGM\test2")
	print valExists(r"HKCU\Software\AGM\test2", "stringValue")
	print valExists(r"HKCU\Software\AGM\test2", "unknownstringValue")
	print getValue(r"HKCU\Software\AGM\test2", "stringValue")
	print getAllValues(r"HKCU\Software\AGM\test2")


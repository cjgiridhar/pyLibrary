import time, datetime, os, calendar

class Timer:
	"""
	Class to work with date, time, calendar
	"""

	def clockTime(self):
		"""
			Returns time as in clock
		"""
		return time.ctime()
	
	def processorTime(self):
		"""
			Returms time for which CPU has worked
		"""
		return time.clock()
	
	def __formatDateTime(self, type):
		year = getattr(type, 'year')
		month = getattr(type, 'month')
		day = getattr(type, 'day')
		hour = getattr(type, 'hour')
		min = getattr(type, 'minute')
		sec = getattr(type, 'second')
		return str(year) + ":" + str(month) + ":" + str(day) + ":" + str(hour) + ":" + str(min) + ":" + str(sec)
		
	def getDateTime(self, timezone = None):
		"""
			Used to print fields for Local or UTC timezones (default: localtime)
			Returns a string with elements in the order as: year, month, day, hour, min, sec, microsecond
		"""
		if timezone is None:
			return self.__formatDateTime(datetime.datetime.now())
		if timezone in ['UTC', 'GMT']:
			return self.__formatDateTime((datetime.datetime.utcnow()))
		else:
			return -1
			
	def timeZone(self):
		"""
			Prints the current time zone
		"""
		return time.tzname[0]

	def getField(self, field, timezone = None):
		"""
			Prints the request field like month, year based on specified timezone (default: localtime)
		"""
		if timezone is None:
			return getattr(datetime.datetime.now(), field)
		if timezone in ['UTC', 'GMT']:
			return getattr(datetime.datetime.utcnow(), field)
		
	def timeStamp(self):
		return str(getattr(datetime.datetime.now(), 'hour')) + str(getattr(datetime.datetime.now(), 'minute')) + str(getattr(datetime.datetime.now(), 'second')) + str(getattr(datetime.datetime.now(), 'microsecond'))
	
	def dateStamp(self):
		return str(getattr(datetime.datetime.now(), 'year')) + str(getattr(datetime.datetime.now(), 'month')) + str(getattr(datetime.datetime.now(), 'day')) 
		
	def datetimeStamp(self):
		return self.dateStamp() + self.timeStamp() 

	def getWeek(self, year, month, week):
		return calendar.monthcalendar(year, month)[1]
		
	def findDay(self, year, month, day):
		date = datetime.date(year, month, day)
		return str(date.ctime()).split(' ')[0]
		
	def getFutureDate(self, dict):
		d1 = datetime.datetime.now()
		FIELDS = [ 'year', 'month', 'days', 'hours', 'minutes', 'seconds', 'microseconds', 'milliseconds', 'weeks']
		for field in FIELDS:
			if field not in dict:
				dict[field]=0
		d2 = d1 + datetime.timedelta(days=dict['days'], seconds=dict['seconds'], microseconds=dict['microseconds'], milliseconds=dict['milliseconds'], minutes=dict['minutes'], hours=dict['hours'], weeks=dict['weeks'])
		return d2
		
if __name__ == '__main()__':
	timer = Timer()
	print "Clock Time:", timer.clockTime()
	print "Date Time in UTC TimeZone:", timer.getDateTime(timezone = 'UTC')
	print "Time Zone:", timer.timeZone()
	print "Hour in localtime:", timer.getField('hour')
	print "Hour in UTC:", timer.getField('hour', timezone = 'UTC')
	print "Time Stamp:", timer.timeStamp()
	print "DateTime Stamp:", timer.datetimeStamp()
	print "CPU Time:", timer.processorTime()
	print "First Week:", timer.getWeek(2011, 7, 1)
	print "The day:", timer.findDay(1984, 6, 4)
	dict = {'days':1, 'hours':2}
	print "Future date:", timer.getFutureDate(dict)

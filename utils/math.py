class Math:
	"""
		Class exporting mathematical algorithms
	"""
	def fib(self, number):
		"""
			Generates nth fibonacci number
		"""
		if number==1:
			return 1
		if number==2:
			return 2
		return self.fib(number-2) + self.fib(number-1)

	def factors(self, number):
		"""
			Generates prime factors of a number
		"""
		list = []
		for num in range(2,int(number**0.5)):
			if number%num == 0:
				list.append(num)
		return list
				
	def isPrime(self, number):
		"""
			Returns 0 if number is prime else returns -1
		"""
		for num in range(2,number-1):
			if number%num == 0:
				return -1
			else:
				continue
		return 0
		
	def isPalindrome(self,number):
		"""
			Returns True if number is palindrome else returns False
		"""
		number = str(number)
		return number == number[::-1]
		
	def sumOfNumbers(self, number):
		"""
			Returns sum of 1st N natural numbers
		"""
		return (number * (number+1))/2

	def sumOfSquares(self,number):
		"""
			Returns sum of squares of 1st N natural numbers
		"""
		return (number * (number+1) * (2*number+1))/6
		
	def isPythagorean(self, num1, num2, num3):
		"""
			Returns 0 if numbers form a Pythagorean template
		"""
		if num3**2 == num2**2 + num1**2:
			return 0
		else:
			return -1
		
	def greatest_common_divisior(self, a, b):
		"""
			Returns greatest common divisior of two numbers
		"""
		return (self.greatest_common_divisior(b,a%b) if b else a)
		
	def least_common_multiple(self, a, b):
		"""
			Returns least common multiple of two numbers
		"""
		return (a*b) / self.greatest_common_divisior(a,b)

if __name__ == '__main()__':
	math = Math()
	print math.greatest_common_divisior(4,6)
	print math.fib(5)
	print math.isPythagorean(3,4,5)
	print math.isPrime(6)

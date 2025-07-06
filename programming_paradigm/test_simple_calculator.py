import unittest
def add(a,b):
	"""Return the sum of two numbers"""
	return a + b

def subtract (a,b):
	"""Return the difference of two numbers"""
	return a - b

def multiply (a, b):
	"""Return the product of two numbers"""
	return a * b

def divide (a , b):
	"""return the  modulus of two numbers"""
	return a / b

class TestAdd(unittest.TestCase):
	def test_add(self):
		result = add(4, 5)
		self.assertEqual(result , 9)

	def test_subtract(self):
		result = subtract(10, 4)
		self.assertEqual(result , 6)

	def test_multiply(self):
		result = multiply(2 , 7)
		self.assertEqual(result, 14)

	def test_divide(self):
		result = divide (4 , 2)
		self.assertEqual(result, 0)

if __name__=="__main__":
	unittest.main()

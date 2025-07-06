import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		"""Sets up a new SimpleCalculatoe instance for each test."""
		self.calc = SimpleCalculator()

	def test_addition(self):
		""" Return the addition of a and b"""
		#result = add(4, 5)
		self.assertEqual(self.calc.add (10 , 10), 20)

	def test_subtraction(self):
		"""Return the difference between a and b"""
		#result = subtract(10, 4)
		self.assertEqual(self.calc.subtract(10,4),6)

	def test_multiplication(self):
		"""Return the product of an and b"""
		#result = multiply(2 , 7)
		self.assertEqual(self.calc.multiply (2,7), 14)

	def test_division(self):
		"""Return the modulus of a and b"""
		#result = divide (4 , 2)
		self.assertEqual(self.calc.divide(20,2),10)

if __name__=="__main__":
	unittest.main()

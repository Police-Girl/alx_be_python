def safe_divide(numerator,denominator):
	try:
		num = float(numerator)
		den = float(denominator)
	except ValueError:
		return f"Error: Please enter numeric values only"
	try:
		result = num/den
		return result
	except ZeroDivisionError:
		return f"Error: Cannot divide by zero"

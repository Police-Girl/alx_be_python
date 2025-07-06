class BankAccount:
	def __init__(self,initial_balance = 0): #idk man, the initial ammount? # with the BA's we just need one attribute??? damn bro.
	#	self.balance = balance
	#	self.deposit = deposit
	#	self.withdraw = withdraw
	#	self.display = display
		self.account_balance = initial_balance
	def deposit(self,amount):	# you did not define this correctly it seemsdef deposit(ammount):
		self.account_balance += amount
		#return f"Deposited{deposit}"
	def withdraw(self, amount):
		if amount <= self.account_balance:
			self.account_balance -= amount
			return True
		else:
			return False
	def display_balance(self):
		print (f"Current Balance: ${self.account_balance}")
			#return f"Current baklance: ${display}"


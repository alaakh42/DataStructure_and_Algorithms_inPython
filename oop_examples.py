class creditCard:
	"""A consumer credit card"""

	def __init__(self, customer, bank, account, limit):
		"""Create a credit card instance"""
		# 		The initial balance is zero.
		# customer the name of the customer (e.g., John Bowman )
		# bank:the name of the bank (e.g., California Savings )
		# acnt:the acount identifier (e.g., 5391 0375 9387 5309 )
		# limit:credit limit (measured in dollars)
		self.customer = customer
		self.bank = bank
		self.account = account
		self.limit = limit
		self.balance = 0

	def get_customer(self):
		return self.customer

	def get_bank(self):
		return self.bank

	def get_account(self):
		return self.account

	def get_limit(self):
		return self.limit

	def get_balance(self):
		return self.balance

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit
		limit. Return True if charge was processed; False if charge was denied."""
		if (price+self.balance > self.limit):
			return False
		else:
			self.balance += price
			return True

	def make_payment(self, amount):
		self.balance -= amount

if __name__ == "__main__":
	wallet = []
	wallet.append(creditCard("Alaa Khaled", "Capital One",
		"5391 0375 9387 5309", 2000))
	wallet.append(creditCard("Tasnem Khaled", "HSBC",
		"5394 0376 9287 5509", 3000))
	wallet.append(creditCard("Sara Khaled", "CIB",
		"5381 2375 9547 5309", 1000))

	for val in range(1, 17):
		wallet[0].charge(val)
		wallet[1].charge(val*2)
		wallet[2].charge(val**2)

	for c in range(3):
		print( 'Customer = ', wallet[c].get_customer( ))
		print( 'Bank = ', wallet[c].get_bank( ))
		print( 'Account = ', wallet[c].get_account( ))
		print( 'Limit = ', wallet[c].get_limit( ))
		print( 'Balance = ', wallet[c].get_balance( ))
	while wallet[c].get_balance( ) > 100:
		wallet[c].make_payment(100)
		print( 'New balance = ', wallet[c].get_balance( ))


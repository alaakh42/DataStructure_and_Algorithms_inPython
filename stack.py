
"""
LIFO
"""
# The Operations of a stack
# s.push()
# s.pop()
# s.top()
# s.is_empty()
# s.is_full()
# len(s)

class ArrayStack:

	def __init__(self):
		self.data = []

	def __len__(self): # O(1)
		return len(self.data)

	def is_empty(self): # O(1)
		return len(self.data) == 0

	def push(self, e): # O(n), where n is the current number of elements in the stack
		self.data.append(e)

	def top(self): # O(1)
		if self.is_empty():
			raise Empty('Stack is empty!')
		return self.data[-1] # return last item in list "top item"

	def pop(self): # O(n)
		if self.is_empty():
			raise Empty('Stack is empty!')
		return self.data.pop() # remove last item in list

if __name__ == "__main__":
	s = ArrayStack()
	s.push(55)
	s.push(52)
	s.push(51)
	s.push(53)
	print s.__len__()
	print s.top()
	print s.__len__()
	print s.pop()

# Application: Matching Delimeters Algorithm

def is_matched(expr):
	lefty = "[{("
	righty = "]})"
	s = ArrayStack()
	for c in expr:
		if c in lefty:
			s.push(c) # push left delimeter in stack
		elif c in righty:
			if s.is_empty(): # if stack is empty and u encounter a right delimeter then this is mismatch
				return False
			if righty.index(c) != lefty.index(s.pop()):
				return False
	return s.is_empty()

print is_matched('( )(( )){([( )])}') # True
print is_matched(')(( )){([( )])}') # False


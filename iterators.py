class SwquenceIterator:
	"""An iterator for any of Python's sequence types"""

	def __init__(self, sequence):
		self.seq = sequence
		self.k = -1  # will increment to 0 on first call to next

	def __next__(self):
		self.k += 1 # advance to next element
		if self.k < len(self.sequence):
			return(self.seq[self.k]) # return the data element
		else:
			raise StopIteration() # there are no more elements

	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator."""
		return self

from timeit import Timer

def example1(S):
	"""Return the sum of the elements with even index in sequence S."""
	n = len(S)
	total = 0
	for j in range(n): # loop from 0 to n-1
	# note the increment of 2
		total += int(S[j])
	return total

def example2(S):
	"""Return the sum of the elements with even index in sequence S."""
	n = len(S)
	total = 0
	for j in range(0, n, 2): # note step=2
	# note the increment of 2
		total += int(S[j])
	return total

def example3(S):
	"""Return the sum of the elements with even index in sequence S."""
	n = len(S)
	total = 0
	for j in range(n): # loop from 0 to n-1
		for k in range(1+j): # loop from 0 to j
	# note the increment of 2
			total += int(S[k])
	return total

def example4(S):
	"""Return the sum of the prefix sums of sequence S."""
	n = len(S)
	prefix = 0
	total = 0
	for j in range(n):
		prefix += int(S[j])
		total += prefix
	return total

def example5(A, B):
	# assume that A and B have equal length
	"""Return the number of elements in B equal to the sum of prefix sums in A."""
	n = len(A)
	count = 0
	for i in range(n): # loop from 0 to n-1
		total = 0
	for j in range(n): # loop from 0 to n-1
		for k in range(1+j): # loop from 0 to j
			total += int(A[k])
	if B[i] == total:
		count += 1
	return count

print ("Ex1: ", str(Timer(lambda: example1("1234")).timeit(number=100)))
print ("Ex2: ", str(Timer(lambda: example2("1234")).timeit(number=100)))
print ("Ex3: ", str(Timer(lambda: example3("1234")).timeit(number=100)))
print ("Ex4: ", str(Timer(lambda: example4("1234")).timeit(number=100)))
print ("Ex5: ", str(Timer(lambda: example5("1234", "1234")).timeit(number=100)))

# ('Ex1: ', '0.000351190567017') O(n)
# ('Ex2: ', '0.000223875045776') O(n+2)
# ('Ex3: ', '0.000962972640991') O(n^2)
# ('Ex4: ', '0.000375032424927')
# ('Ex5: ', '0.00150179862976')


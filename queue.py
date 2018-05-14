"""
FIFO
"""
# The operations of a queue
# q.queue(s)
# q.dequeue()
# q.first()
# q.is_empty()
# len(q)

class ArrayQueue:
	DEFAULT_CAPACITY = 10
	
	def __init__(self):
		self.data = [None]*ArrayQueue.DEFAULT_CAPACITY
		self.size = 0
		self.front = 0

	def __len__(self): # O(1)
		return self.size 

	def is_empty(self): # O(1)
		return self.size == 0

	def first(self): # O(1)
		"""Return (but do not remove) the element at the front of the queue"""
		if self.is_empty():
			raise Empty("The queue is empty!")
		return self.data[self.front]

	def dequeue(self): # O(n), where n is the number of elements in the queue 
		"""Remove and return the first element of the queue i.e. FIFO"""
		if self.is_empty():
			raise Empty("The queue is empty!")
		answer = self.data[self.front]
		self.data[self.front] = None # help garbage collection
		self.front = (self.front+1)%len(self.data)
		self.size -= 1
		return answer 

	def enqeue(self, e): #O (n)
		"""Add elemet tothe back of the queue"""
		if self.size == len(self.data): # queue is full
			# raise print("Queue is empty")
			self.resize(2*len(self.data)) # double the size of the queue
		avail = (self.front + self.size)%len(self.data) # to compute the location of next openning
		self.data[avail] = e
		self.size += 1

	def resize(self, capacity):
		"""Resize to a new list of capacity >= len(self)."""
		old = self.data # keep track of existing list
		self.data = [None]*cap # allocate list with new capacity
		walk = self.front 
		for k in range(self.size): # only consider existing elements
			self.data[k] = old[walk] 	# intentionally shift indices
			walk = (1 + walk) % len(old) # use old size as modulus
		self.front = 0 # front has been realigned

if __name__ == '__main__':
	q = ArrayQueue()
	q.enqeue(5)
	q.enqeue(3)
	print len(q)
	print q.dequeue()
	print q.is_empty()
	print q.dequeue()
	print q.is_empty()
	try:
		print q.dequeue()
	except:
		print "Error"
	q.enqeue(7)
	q.enqeue(9)
	print q.first()
	q.enqeue(4)
	print len(q)
	print q.dequeue()


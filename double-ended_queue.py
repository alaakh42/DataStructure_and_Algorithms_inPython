"""
This queue supports insertion and deletion from both ends (the front and the back of a queue),
for short itis called `deque` pronounced `deck`
"""
# The methods in a double-ended queue
# d.add_first(e)
# d.add_last(e)
# d.delete_first(e) # return and remove
# d.delete_last(e) # return and remove
# # The accessors of a double-ended queue
# d.first() # return but don't remove
# d.last() # return but don't remove
# d.is_empty()
# len(d)

class DoubleEndedQueue:
	QUEUE_CAPACITY = 10

	def __init__(self):
		self.data = [None]*DoubleEndedQueue.QUEUE_CAPACITY
		self.front = 0
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def first(self):
		if self.is_empty():
			raise Empty("The deque is empty!")
		answer = self.data[self.front]
		return answer

	def last(self):
		if self.is_empty():
			raise Empty("The deque is empty!")
		back = (self.front+self.size-1)%len(self.data) # index of last element in queue
		return self.data[back]

	def add_first(self, e):
		front = (self.front+self.size)%len(self.data)
		self.data[front] = e
		self.size += 1
		self.front = (self.front-1)%len(self.data)

	def add_last(self, e):
		last = (self.front+self.size-1)%len(self.data)
		self.data[last] = e
		self.size += 1
		self.last = (self.front+self.size-1)%len(self.data)

	def delete_first(self):
		answer = self.data[self.front]
		self.size -= 1 
		self.front = (self.front+1)%len(self.data)
		return answer

	def delete_last(self):
		answer = self.data[self.last]
		self.size -= 1
		self.last = (self.last-1)%len(self.data) 
		return answer

if __name__ == '__main__':
	d = DoubleEndedQueue()
	d.add_last(5)
	d.add_first(3)
	d.add_first(7)
	print d.first
	print d.delete_last()
	print len(d)
	print d.delete_last()
	print d.delete_last()
	d.add_first(6)
	print d.last
	d.add_first(8)
	print d.is_empty()
	print d.last
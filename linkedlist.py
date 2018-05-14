"""
1. Singly linked list
a linear sequence of nodes, wach node has a refrence to a sequence element plus
the next node of the list,
"""

# Implementing Stack with a singly linked list
# where the head of the linked list represents the top of the stack

class LinkedStack:
	"""LIFO stack implemetation using a singly linked list for storage"""
	# Nested _Node class
	class _Node:
		"""a class for storing a singly linked node"""
		__slot__ = element, _next

		def __init__(self, element, _next):
			self.element = element
			self._next = _next

		# Stack methods
		def __init__(self):
			self.head = None
			self.size = 0

		def __len__(self): # O(1)
			return self.size

		def is_empty(self): # O(1)
			return self.size == 0

		def push(self, e): # O(1)
			self.head = self.Node(e, self.head) # create and link a new node
			self.size += 1

		def top(self): # O(1)
			if self.is_empty():
				raise Empty("Stack is empty!")
			answer = self.head.element
			return answer

		def pop(self): # O(1)
			if self.is_empty():
				raise Empty("Stack is empty!")
			answer = self.head.element
			self.size -= 1
			self.head = self.head._next
			return answer

# Implementing Queue with a singly linked list
# 
class LinkedQueue:
	"""FIFO queue implemetation using a singly linked list"""
	class _Node:

		def __init__(self, element, _next):
			self.element = element
			self._next = _next

		def __init__(self):
			"""create an empty queue"""
			self.head = None
			self.tail = None
			self.size = 0

		def __len__(self):
			return self.size

		def is_empty(self):
			return self.size == 0

		def first(self): # O(1)
			"""Return (but do not remove) the element at the front of the queue"""
			if self.is_empty():
				raise Empty("The queue is empty!")
			return self.head.element

		def dequeue(self): # O(n), where n is the number of elements in the queue 
			"""Remove and return the first element of the queue i.e. FIFO"""
			if self.is_empty():
				raise Empty("The queue is empty!")
			answer = self.head.element
			self.head = self.head.next
			self.size -= 1
			if self.is_empty():
				self.tail = None
			return answer 

		def enqeue(self, e): # O(n)
			"""Add elemet to the back of queue"""
			newest = self.Node(e, None)# new node wil be new tail node
			if self.is_empty(): # if a queue is empty
				self.head = newest # your new element is the new head
			else:
				self.tail.next = newest # if not empty it is next to the tail
			self.tail = newest # if there is only one element in queue
			self.size += 1






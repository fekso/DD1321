
class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class LinkedQ:
	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, item):
		node = Node(item)
		if self.isEmpty(): 
			self.first = node
			self.last = node
		else: 
			self.last.next = node
			self.last = node

	def dequeue(self):
		node = self.first
		if self.first != self.last: 
			self.first = node.next
		else: #tömmer kön
			self.first = None
			self.last = None
		return node.value 

	def isEmpty(self): 
		if(self.first == None):
			return True
		else:
			return False

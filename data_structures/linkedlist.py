# Implementing a singly Linked List
class Node(object):

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

	# Search for the Linked List node containing a specific data value and return the node
	# Time Complexity: O(n)
	def search(self, data):
		current = self
		found = False
		while current != None and found == False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list!")
		return current

	
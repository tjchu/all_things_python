# Implementing a singly Linked List
class ListNode(object):

	def __init__(self, data=None, next_node=None):
		self.val = data
		self.next = next_node

	def get_val(self):
		return self.val

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

# Search for the Linked List node containing a specific data value and return the node
# Time Complexity: O(n)
def search(node: ListNode, data):
	current = node
	found = False
	while current != None and found == False:
		if current.get_val() == data:
			found = True
		else:
			current = current.get_next()
	if current is None:
		raise ValueError("Data not in list!")
	return current



def addTwoNumbers(self, l1: ListNode, l2: ListNode)
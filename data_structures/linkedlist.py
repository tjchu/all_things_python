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
def search(node: ListNode, data) -> ListNode:
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

# Detect if a LinkedList has a cycle
def hasCycle(head: ListNode) -> boolean:
	# If there is no or only one LinkedList node, a cycle cannot happen so return False
	if head == None or head.next == None:
		return False

	# Create a slow and fast node where the fast one will traverse through the LinkedList faster
	# and will eventually run into the slower node if there is a cycle or run to the end of the list
	# if there isnt a cycle
	slow = head
	fast = head.next
	while fast != None and fast.next != None:
		if fast == slow:
			return True
		slow = slow.next
		fast = fast.next.next
	return False


# Reverse LinkedList with a stack
# O(n)
def reverseLinkedListwStack(head: ListNode) -> ListNode:
	stack = []
	curr = head

	# Check if it's a non-existent or single node because can't really reverse that
	if curr == None or curr.next == None:
		return curr
	# Traverse through the LinkedList and push onto the stack
	while curr:
		stack.add(curr)
	# Pop the stack and
	new_head = stack,pop()
	node = new_head
	while len(stack):
		node.set_next(stack.popo())
		node = node.get_next()



"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	head = ListNode(0)
	root = head
	carry = False
    
    while l1 or l2 or carry:
		sum = 0
		if l1:
			sum += l1.val
			l1 = l1.next
		if l2:
			sum += l2.val
			l2 = l2.next
		if carry: 
			sum += 1
			carry = False
		if sum >= 10:
			sum = sum % 10
			carry = True

	head.next = ListNode(sum)
	head = head.next
	return root.next


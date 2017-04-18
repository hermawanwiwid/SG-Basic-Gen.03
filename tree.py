class Node:
	def __init__(self, val):
		self.info = val
		self.left = None
		self.right = None

	def insert(self, val):
		if val <self.info:
			if self.left is None:
				self.left = Node(val)
			else:
				self.left.insert(val)
		elif val > self.info:
			if self.right is None:
				self.right = Node(val)
			else:
				self.right.insert(val)

	def inOrder(self):
		if self.left:
			self.left.inOrder()
		print(self.info, end=" ")
		if self.right:
			self.right.inOrder()

	def postOrder(self):
		if self.right:
			self.right.inOrder()
		if self.left:
			self.left.inOrder()
		print(self.info, end=" ")

	def preOrder(self):
		print(self.info, end=" ")
		if self.right:
			self.right.inOrder()
		if self.left:
			self.left.inOrder()

	def search(self,val):
		if (val < self.info):
			if self.info:
				return self.left.search(val)
			else:
				return False
		if (val > self.info):
			if self.info:
				return self.right.search(val)
			else:
				return False
		else:
			return True

	def sizee(self):
		total = 1
		if self.left is not None:
			total += self.left.sizee()
		if self.right is not None:
			total += self.right.sizee()
		return total

	    
BT = Node(23)
BT.insert(10)
BT.insert(16)
BT.insert(19)
BT.insert(65)
BT.insert(45)
BT.insert(24)
BT.insert(67)
BT.insert(30)
BT.inOrder()
print (" InOrder")
BT.preOrder()
print (" PreOrder")
BT.postOrder()
print (" PostOrder")
BT.sizee()




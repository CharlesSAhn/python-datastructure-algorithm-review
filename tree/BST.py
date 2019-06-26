# BST - a binary search tree relies on the proper that keys that are less than the parent found in the left subtree and keys that are
# greater than the parent are found in the right tree.

class TreeNode:

	def __iter__(self, key, val, left=None, right=None, parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLefthild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not(self.leftChild or self.rightChild)

	def hasAnyChild(self):
		return self.rightChild or self.leftChild

	def hasBothChild(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self, key, value, lc, rc):
		self.key = key
		self.payload = value
		self.leftChild = lc
		self.rightChild = rc
		
		if self.hasLeftChild():
			self.leftChild.parent = self

		if self.hasRightChild():
			self.rightChild.parent = self


class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	#allows you to len() to get the size
	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()
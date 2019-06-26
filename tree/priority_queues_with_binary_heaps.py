# acts like a queue in thtat you dequeue an item by removing it from the front.
# however, in a priority queue the logical order of items inside a queue is determined by their priority
# The highest priority items are att the front of the queue and the lowest priority items are at the back.
# when you enqueue an item on a priority queue, the new item may move all the way to the front.

# THe classic way to implement a priority queue is using a data structure called a binary heap.
# a binary heap will allow us both enqueue and dequeue itmes in O(log n)

# min heap: smallest key is always at the front.
# max heap: the largest key value is always at the front.

# we will implement the min key.

# we will use the binary tree and must keep our tree balanced


class BinHeap:

	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)


	def percUp(self, i):

		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]

				self.heapList[i] = tmp

			i = i // 2


	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)

			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp

			i = mc


	def minChild(self, i):
		if i * 2 +1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1


	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)

		return retval

	def buildHeap(self, alist):

		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i-1
# A hash table is a collection of items which are stored in such a way that it makes easy tp find them later.
# Each position of the hash table, slots, can hold an item and is named by an integer value starting at 0.

# The mapping between an item and the slot where that items belongs in the hash table is called the hash function.
# The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1
#   item % 11  = hash value

# load factor = # of items/ table size.

#Hash function = maps each item iun

# collision: reference to a collection of items.  (chaining)

class HashTable(object):

	def __init__(self, size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data):
		hashValue = self.hashFunction(key, len(self.slots))

		if self.slots[hashValue] == None:
			self.slots[hashValue] = key
			self.data[hashValue] = data

		else:
			if self.slots[hashValue] == key:
				self.data[hashValue] = data

			else:
				nextslot = self.rehash(hashValue, len(self.slots))

				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data



	def hashFunction(self, key, size):
		return key % size


	def rehash(self, oldhash, size):
		return (oldhash + 1) % size

	def get(self, key):

		startslot = self.hashFunction(key, len(self.slots))
		data = None
		stop = False
		found = False
		position = startslot

		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True

		return data
# Stack() creates a new stack that is empty
# push()
# pop()
# peek() - returns the top item from the stack but does not remove it.
# isEmpty() - tests to see whether the stack is empty
# size()


class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(1)
s.push("Two")
print(s.peek())
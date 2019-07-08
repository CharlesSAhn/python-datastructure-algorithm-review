
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.size()


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None



class QueueLinkedList():

    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        return self.head == None

    #insert at the end
    def enqueue(self, item):
        newNode = Node(item)

        #if self.tail == None -> queue is empty.
        if self.tail is None:
            self.head = self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode

    #remove from the beginning
    def dequeue(self):
        if self.isEmpty():
            return

        tmp = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return tmp


q = QueueLinkedList()

print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.isEmpty())
print(q.dequeue().value)
print(q.dequeue().value)
print(q.dequeue().value)
print(q.isEmpty())
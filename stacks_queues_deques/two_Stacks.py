
class Queue2Stacks(object):

    def __init__(self):

        self.instack = []
        self.outstack= []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):

        if len(self.outstack) == 0:
            while len(self.instack) > 0:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)


for i in range(5):
    print(q.dequeue())
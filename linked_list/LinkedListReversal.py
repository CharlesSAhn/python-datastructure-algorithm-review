# Function that reverse a linked list in place. The function will take in the head of the list as input and return
# the new head of the list.

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(node):

    current = node
    previous = None
    next = node.nextnode

    while next.nextnode is not None:
        current.nextnode = previous

        previous = current
        current = next
        next = next.nextnode

    return next



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(reverse(a).value)

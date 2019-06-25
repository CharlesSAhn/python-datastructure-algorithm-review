class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None



def nth_to_last_node(k, n):
    pointer1 = n
    pointer2 = n

    if k < 1:
        raise LookupError('Error')

    for i in range(k):

        if not pointer2.nextnode:
            raise LookupError('Error')
        pointer2 = pointer2.nextnode

    while pointer2 is not None:
        pointer1 = pointer1.nextnode
        pointer2 = pointer2.nextnode

    return pointer1.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(nth_to_last_node(0, a))
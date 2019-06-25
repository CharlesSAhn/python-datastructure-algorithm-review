


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker1 != None and marker2.nextnode != None and marker2.nextnode.nextnode != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        print(marker2)

        if marker1 == marker2:
            return True

    return False





# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = a
#
# print(cycle_check(a))



x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y


print(cycle_check(x))
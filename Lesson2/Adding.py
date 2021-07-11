"""
This code is going to first set up the class for each element of the linked list
and then the class for the linked list
"""

############################
# Element class
############################

class element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# NOTE:
# The above code sets up the element for the element
# An element has some value associated with it,
# and it has a variable that points to the next element in then
# linked list.

############################
# Linkedlist class
############################

class Linkedlist(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


e1 = element(1)
e2 = element(2)
e3 = element(3)
e4 = element(4)

x = Linkedlist(e1)
x.append(e2)
x.append(e3)
x.append(e4)


print(x.head.next.value)

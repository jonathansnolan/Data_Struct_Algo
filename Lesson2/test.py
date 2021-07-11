from LinkedListSetUp import element
from LinkedListSetUp import Linkedlist

# Set your Elements
e1 = element("Jonathan")
e2 = element("Nolan")

LL = Linkedlist(e1)
LL.append(e2)

print(LL.head.value)
print(LL.head.next.value)

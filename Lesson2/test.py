
#from LinkedListSetUp import *

from LinkedListSetUp import element
from LinkedListSetUp import Linkedlist

#################################
# NOTE:
# You have to import the necessary classes individually it seems
# Alternatively, you can use the following code:
# from LinkedListSetUp import *

################################
# Set your Elements
################################

e1 = element("Jonathan")
e2 = element("Nolan")

################################
# Make your LinkedList
################################
LL = Linkedlist(e1)
LL.append(e2)

print(LL.head.value)
print(LL.head.next.value)

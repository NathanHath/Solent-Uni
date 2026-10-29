from node import Node
from LinkedList import linkedlist
myList = linkedlist()
n1 = Node("Fred")
n2 = Node("Tom")
n3 = Node("Bob")
myList.add(n1)
myList.add(n2)
myList.add(n3)
index = int(input("Please enter an index: "))
found_node = myList.get(index)
print(found_node)

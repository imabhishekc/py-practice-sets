# Creating a simple singly Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creating Nodes
node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
node5 = Node(500)

# Connecting nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Printing the linked list
current = node1
while current is not None:
    print(current.data, end="-->")
    current = current.next
print("None")
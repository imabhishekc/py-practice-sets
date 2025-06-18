class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next

        # Attach new node at the end
        current.next = new_node

    def print_list(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(100)
    ll.insert_at_end(200)
    ll.insert_at_end(300)
    ll.insert_at_end(400)
    ll.insert_at_end(500)

    ll.print_list()
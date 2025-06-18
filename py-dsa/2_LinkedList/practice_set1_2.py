"""Implementing doubly linked list."""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        pass

    def insert_values(self, data_list):
        pass

    def get_length(self):
        pass

    def remove_at(self, index):
        pass

    def insert_at(self, index, data):
        pass

    def insert_after_value(self, data_after, data_to_insert):
        pass

    def remove_by_value(self, data):
        pass
    
    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        pass

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        pass


if __name__ == '__main__':
    dll = DoublyLinkedList()

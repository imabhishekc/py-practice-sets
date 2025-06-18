"""Implementing doubly linked list."""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, next=self.head)
        
        if self.head:
            self.head.prev = node
        else:
            self.tail = node

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
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next
        print(dllstr + "None")

    def print_backward(self):
        itr = self.tail
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '<--'
            itr = itr.prev
        print(dllstr + "None")


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(23)
    dll.print_forward()
    dll.print_backward()
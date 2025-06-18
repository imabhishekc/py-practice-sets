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
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

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
    dll.insert_at_end(54)
    dll.print_forward()
    dll.print_backward()
    print("length:", dll.get_length())
    dll.insert_values(['lion', 'tiger', 'leopard', 'panther'])
    dll.print_forward()
    dll.print_backward()
    print("length:", dll.get_length())
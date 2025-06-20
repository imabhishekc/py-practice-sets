class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
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
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            
            itr = itr.next
        print(f"Value '{data_after}' not found in list")

    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['lion', 'tiger', 'leopard'])
    ll.print()                                  # lion-->tiger-->leopard-->

    ll.insert_at_beginning('panther')
    ll.print()                                  # panther-->lion-->tiger-->leopard-->

    ll.insert_at_end('cheetah')
    ll.print()                                  # panther-->lion-->tiger-->leopard-->cheetah-->

    ll.insert_at(2, 'cat')
    ll.print()                                  # panther-->lion-->cat-->tiger-->leopard-->cheetah--> 

    ll.remove_at(3)
    ll.print()                                  # panther-->lion-->cat-->leopard-->cheetah-->

    print("Length:", ll.get_length())           # prints 'Length: 5'

    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()                                  # banana-->mango-->grapes-->orange-->

    ll.insert_after_value("mango","apple")      # insert apple after mango
    ll.print()                                  # banana-->mango-->apple-->grapes-->orange-->

    ll.remove_by_value("orange")                # remove orange
    ll.print()                                  # banana-->mango-->apple-->grapes-->

    ll.remove_by_value("figs")                  # remove figs (It is not in the list so nothing happens)
    ll.print()                                  # banana-->mango-->apple-->grapes-->

    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()                                  # prints 'Linked list is empty'
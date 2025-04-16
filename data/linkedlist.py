#!/usr/bin/env python

class LinkedList:
    def __init__(self):
        self.first_n = None

    def get_smallest(self):
        if self.first_n != None:
            return self.first_n.get_item()
        else:
            return None

    def insert_item(self, item):
        if self.first_n == None:                      # 1.
            newnode = Node(item)
            self.first_n = newnode
        else:
            if item < self.first_n.get_item():        # 2a.
                newnode = Node(item)                      # 1)
                newnode.set_next_n(self.first_n)          # 2)
                self.first_n = newnode                    # 3)
            else:                                     # 2b.
                self.first_n.insert_item(item)
    
    def is_item_present(self, query) -> bool:
        if self.first_n == None:
            return False
        else:
            answer = self.first_n.is_item_present(query)
            return answer

class Node:
    def __init__(self, item):
        self.item = item
        self.next_n = None

    def get_item(self):
        return self.item

    def get_next_n(self):
        return self.next_n

    def set_next_n(self, newnext):
        self.next_n = newnext

    def insert_item(self, item):
        if self.next_n == None:
            newnode = Node(item)
            self.next_n = newnode
        else:
            if item < self.next_n.get_item():
                newnode = Node(item)
                newnode.set_next_n(self.next_n)
                self.next_n = newnode
            else:
                self.next_n.insert_item(item)
    
    def is_item_present(self, query) -> bool:
        if self.item == query:                         # 1.
            return True
        else:
            if self.next_n == None:                    # 2a.
                return False
            else:                                      # 2b.
                answer = self.next_n.is_item_present(query)
                return answer

if __name__ == "__main__":
    numlist = LinkedList()
    numlist.insert_item(9)
    numlist.insert_item(3)
    numlist.insert_item(7)
    print(numlist.get_smallest())       # prints 3
    numlist.insert_item(2)
    print(numlist.get_smallest())       # prints 2
    print(numlist.is_item_present(7))   # prints True
    print(numlist.is_item_present(6))   # prints False
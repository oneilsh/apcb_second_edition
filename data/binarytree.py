#!/usr/bin/env python

class BinaryTree:
    def __init__(self):
        self.root_n = None

    def insert_item(self, item):
        if self.root_n == None:
            newnode = Node(item)
            self.root_n = newnode
        else:
            self.root_n.insert_item(item)
    
    def get_smallest(self):
        if self.root_n == None:
            return None
        else:
            answer = self.root_n.get_smallest()
            return answer

class Node:
    def __init__(self, item):
        self.item = item
        self.left_n = None
        self.right_n = None
        
    def get_item(self):
        return self.item
    
    def get_left_n(self):
        return self.left_n
    
    def set_left_n(self, newleft):
        self.left_n = newleft
        
    def get_right_n(self):
        return self.right_n
    
    def set_right_n(self, newright):
        self.right_n = newright

    def insert_item(self, item):
        if item < self.item:                        
            if self.left_n == None:                 # 1a.  
                newnode = Node(item)
                self.left_n = newnode
            else:                                   # 1b.
                self.left_n.insert_item(item)
        else:
            if self.right_n == None:                # 2a.
                newnode = Node(item)
                self.right_n = newnode
            else:                                   # 2b.
                self.right_n.insert_item(item)
                

    def get_smallest(self):
        if self.left_n == None:
            return self.item
        else:
            answer = self.left_n.get_smallest()
            return answer


numtree = BinaryTree()
numtree.insert_item(9)
numtree.insert_item(3)
numtree.insert_item(7)
numtree.insert_item(1000)
numtree.insert_item(10)
print(numtree.get_smallest())       # prints 3
numtree.insert_item(2)
print(numtree.get_smallest())       # prints 2

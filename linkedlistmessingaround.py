class LinkedList:
    def __init__(self):
        self.length = 0
        self.head   = None

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1
        
   def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()
        print "]",

class Node:
    ...
    def print_backward(self):
    if self.next != None:
        tail = self.next
        tail.print_backward()
    print self.cargo,
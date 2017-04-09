
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
        print "]"





class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
    	if self.next != None:
    		tail = self.next
    		tail.print_backward()
    	print self.cargo,


def print_list(node):
	print '[',

	while node:
		print node,  # why does this comma list the prints in one line
		print',',
		node = node.next
	print ']'
# if I wanted to impliment this inside the class node how would I. Why is that a bad idea.
# A: call self in the print self and then self.printlist when I Wanted to use it, because I coulnd't use it with the empty list

#def print_backward(list):
#    if list == None:
#    	return
#    head = list
#    tail = list.next
#    print_backward(tail)
#    print head,




#why would I want to list infiniatly or recurse infinitly.  ( ie: nodes refurring back to themselves.)
# why would I want to prove that print list and print backward terminate? :
#: example: tound robin scheduling for an OS 
#with a precondition of no loops- I can definitivly say it will terminate. 

#def print_backward(list) :
#    if list == None : return
#    print_backward(list.next)
#    print list,
# this creates every element- and because of how it recursivly calls itself the first to terminate and actually print is the last element- and then it folds upward? 
# also this is the exact same as the other method- or a looping method so why one v the other v the other?

# The fundamental ambiguity theorem describes the ambiguity that is inherent in a reference to a node: A variable that refers to a node might treat the node as a single object or as the first in a list of nodes.


def removeSecond(list):
    if list == None:
    	return
    first = list
    second = list.next
# make the first node refer to the third
    first.next = second.next
# separate the second node from the rest of the list
    second.next = None
    return second




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print node1
print node2
print node3

print_list(node1)

node1.print_backward()
print ''


ltrial = LinkedList()
ltrial.addFirst(5)
ltrial.print_backward()








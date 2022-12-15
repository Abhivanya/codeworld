# most important interview questions series
# python program to reverse a linked list

# Node class

class Node:
    # Initalizating constructor the node object
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    # creating a fucntion to initializing head
    def __init__(self):
        self.head = None

    # Function to reverse a linkdc list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    # function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # fucntion to print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked Lists si : ")
llist.printList()
llist.reverse()

print(' \nReversed Linked lists is : ')
llist.printList()
'''
linked list 기초

'''

# node
class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data


# 5 -> 1
class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_lsit = ''
        while temp:
            linked_lsit += (str(temp.data) + ' ')
            temp = temp.next

        print(linked_lsit)


list = LinkedList()

list.head = Node(5)

second = Node(1)
third = Node(4)

forth = Node(2)

list.head.next = second
second.next = third
third.next = forth

list.printList()


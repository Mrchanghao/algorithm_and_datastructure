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

    def print_list(self):
        temp = self.head
        linked_list = ''
        while temp:
            linked_list += (str(temp.data) + '--> ')
            temp = temp.next

        print(linked_list)

    def insertion_list(self, val, pos):
        target = Node(val)
        if(pos == 0):
            target.next = self.head
            self.head = target
            # return
        def getPrev(pos):
            temp = self.head
            count = 1
            while count < pos:
                temp = temp.next
                count += 1
            return temp

        prev = getPrev(pos)
        next_node = prev.next
        prev.next = target
        target.next = next_node

    # def delete_node(self, key):


# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def printList(self):
#         temp = self.head
#         linked_lsit = ''
#         while temp:
#             linked_lsit += (str(temp.data) + ' ')
#             temp = temp.next
#
#         print(linked_lsit)

#  5 -> 1 -> 4 -> 2
list = LinkedList()

list.head = Node(5)

second = Node(1)
third = Node(4)

forth = Node(2)

list.head.next = second
second.next = third
third.next = forth

list.insertion_list(3, 2)
# 5 -> 1 -> 3 -> 4 -> 2
list.print_list()


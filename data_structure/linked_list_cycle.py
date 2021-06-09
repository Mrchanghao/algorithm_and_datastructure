'''
linked list가 연결 되어 있는지 체크



'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# inserting node

class LinkkedList(object):
    def __init__(self):
        self.head = None

    # O(1)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if(self.head is None):
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('previous node must in liknked list')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            if temp.value != None:
                print(temp.value, end=' --> ')


            temp = temp.next


def hasCycle(self, head):
    if not head:
        return False

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False




list = LinkkedList()

list.append(4)
list.append(1)
list.append(2)
list.push(5)
list.push(10)
list.print_list()
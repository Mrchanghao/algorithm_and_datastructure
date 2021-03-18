'''
linked list가 연결 되어 있는지 체크



'''


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = None


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

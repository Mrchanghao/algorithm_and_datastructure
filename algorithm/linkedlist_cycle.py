'''
linked list가 cycle인지 아닌지
'''

def has_cycle(head):
    if(head == None):
        return False

    slow = head
    fast = head.next

    while slow != fast & fast != None:
        if fast.next == None:
            return False
        fast = fast.next.next
        slow = slow.next

    if slow == fast:
        return True

    return False


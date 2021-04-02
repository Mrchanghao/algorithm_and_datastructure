'''
1 -> 2 -> 2 -> 1
return true

linked list 가 panlindrome 인지 check

'''

# value를 array로 한다음 체크

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# def isPanlindrome(head):
#     arr = []
#
#     while head != None:
#         arr.append(head.data)
#         head = head.next
#     i = 0
#     j = len(arr) - 1
#
#     while i <= j:
#         if arr[i] != arr[j]:
#             return False
#         i += 1
#         j -= 1
#
#     return True

# apporach 2
# runner
def isPanlindrome(head):
    slow, fast, prev = head, head, None

    if fast == None or fast.next == None:
        return True

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        prev = slow

    prev.next = None

    if fast != None:
        return check(head, reverse(slow.next))

    else:
        return check(head, reverse(slow))


def check(head1, head2):
    while head1 != None and head2 != None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

def reverse(head):
    curr = head
    prev = None
    next = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
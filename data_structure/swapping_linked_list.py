'''
k번째 node와
끝에서 k번째 노드를 서로 스왑 해라

1 > 2 > 3 > 4
k = 2

result ==> 1 > 3> 2 > 4
'''
# fast
# slow
# first and second 이용

class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val


def swap_linekd_list(head, k):
    # fast = head
    # slow = head
    #
    # first = head
    # second = head
    #
    # for i in range(0, k - 1):
    #     fast = fast.next
    #
    # first = fast
    #
    # while fast.next != None:
    #     slow = slow.next
    #     fast = fast.next
    #
    # second = slow
    #
    # second.val, first.val = first.val, second.val
    #
    # return head
    if not head.next:
        return head

    one = two = three = head
    # get the kth node beginning
    for _ in range(k - 1):
        one = one.next
        two = two.next
        # get the kth node from behind
    while two.next:
        two = two.next
        three = three.next

#     swap
    three.val, one.val = one.val, three.val

    return head


# leetcode hint

def solutin(head, k):
    res = []
    curr = head

    while curr is not None:
        res.append(curr)
        curr = curr.next
    res[k - 1].val, res[len(res) - k].val = res[len(res) - k].val, res[k - 1].val

    return head

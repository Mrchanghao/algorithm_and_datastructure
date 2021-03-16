class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
   1        1
  / \      /  \
 /   \    /    \
 2    3   2     3   --> 바이너리 트리가 같은 트리 값인지 확인   --> true 
'''


# recursion
# isSameTree(self, )

class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

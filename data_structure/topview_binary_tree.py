'''
        1
       /   \
      2     3
     / \    /  \
    4   5  6   7

 return 4 2 1 3 7
'''

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def fillMap(root, d, l, m):
    if (root == None):
        return
    if d not in m:
        m[d] = [root.data, l]
    elif m[d][1] > l:
        m[d] = [root.data, l]
    fillMap(root.left, d - 1, l + 1, m)
    fillMap(root.right, d + 1, l + 1, m)

def topView(root):
    m = {}
    fillMap(root, 0, 0, m)
    for it in sorted(m.keys()):
        print(m[it][0], end=" ")


# Driver Code
if __name__ == '__main__':
    """ Create following Binary Tree
            1
        / \
        2 3
        \
            4
            \
            5
            \
                6*
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print("Following are nodes in top",
          "view of Binary Tree")
    topView(root)

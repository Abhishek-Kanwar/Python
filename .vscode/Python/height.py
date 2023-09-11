class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def MaxDepth(node):
    if node is None:
        return 0
    else:
        ldepth = MaxDepth(node.left)
        rdepth = MaxDepth(node.right)
    
    if(ldepth > rdepth):
        return ldepth+1
    else:
        return rdepth+1

def identical(a, b):
    if a is None and b is None:
        return True
    if a in not None and b is not None:
        return((a.data == b.data) && identical(a.left, b.left) && identical(a.right, b.right))

    return False
    
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Height of tree is %d" % (MaxDepth(root)))    

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


m = 1
d = 1

def sol(t: TreeNode):
    global d
    global m

    if t is None:
        return 0

    if t.left:
        d += 1
        m = max(d, m)

        sol(t.left)
        d -= 1
    if t.right:
        d += 1
        m = max(d, m)

        sol(t.right)
        d -= 1

    return m

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(5)


print(sol(t))

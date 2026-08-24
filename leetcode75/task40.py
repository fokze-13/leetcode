class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol(root: TreeNode) -> int:
    stack = [(root, "root", 0)]
    m = 0

    while stack:
        node, direction, cnt = stack.pop()

        m = max(cnt, m)

        if node.right:
            t = (node.right, "right", 1)

            if direction in ("root", "left"):
                t = (node.right, "right", cnt + 1)

            stack.append(t)

        if node.left:
            t = (node.left, "left", 1)

            if direction in ("root", "right"):
                t = (node.left, "left", cnt + 1)

            stack.append(t)

    return m
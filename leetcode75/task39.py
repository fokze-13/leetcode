from collections import deque



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def dfs(root: TreeNode) -> list[int]:
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def bfs(root: TreeNode) -> list[int]:
    res = []
    queue = deque([root])

    while queue:
        curr = queue.popleft()
        res.append(curr.val)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return res


r = TreeNode(3)
r.left = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(2)

def sol(root: TreeNode) -> int:
    c = 0
    stack = [(root, root.val)]

    while stack:
        node, m = stack.pop()

        if node.val >= m:
            m = node.val
            c += 1

        if node.right:
            stack.append((node.right, m))
        if node.left:
            stack.append((node.left, m))

    return c


print(dfs(r))
print(bfs(r))
print(sol(r))

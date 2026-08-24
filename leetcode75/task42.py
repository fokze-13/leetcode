class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sol(root: TreeNode) -> list[int]:
    queue = [root]
    res = []

    while queue:
        new_queue = []

        res.append(queue[0].val)

        for node in queue:
            if node.right:
                new_queue.append(node.right)

            if node.left:
                new_queue.append(node.left)

        queue = new_queue

    return res

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(5)
r.right.right = TreeNode(4)

print(sol(r))

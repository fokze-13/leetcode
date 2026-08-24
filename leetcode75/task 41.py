class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


def sol(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    stack = [(root, ["root"])]
    paths = []

    while stack:
        node, path = stack.pop()

        if node.val in (p.val, q.val):
            paths.append(path)

            if len(paths) == 2:
                break

        if node.right:
            new_path = path.copy()
            new_path.append("right")

            stack.append((node.right, new_path))
        if node.left:
            new_path = path.copy()
            new_path.append("left")

            stack.append((node.left, new_path))

    node = root
    for l, r in zip(paths[0], paths[1]):
        if l != r:
            break
        else:
            if l == "left":
                node = node.left
            elif l == "right":
                node = node.right

    return node

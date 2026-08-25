from leetcode75.task37 import TreeNode


def sol(root: TreeNode, val: int) -> TreeNode | None:
    node = root

    while node.val != val:
        if val < node.val:
            if node.left:
                node = node.left
            else:
                return None
        else:
            if node.right:
                node = node.right
            else:
                return None

    return node
from task42 import TreeNode


def sol(root: TreeNode) -> int:
    queue = [root]

    level = 1
    max_sum = root.val
    max_sum_level = 1

    while queue:
        s = 0
        new_queue = []

        for node in queue:
            s += node.val

            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)

        if s > max_sum:
            max_sum = s
            max_sum_level = level

        queue = new_queue
        level += 1

    return max_sum_level


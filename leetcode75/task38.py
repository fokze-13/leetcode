from typing import Optional
from task37 import TreeNode


def sol(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    leafs1 = []
    leafs2 = []

    def sol1(t1: TreeNode):
        nonlocal leafs1

        if t1.left:
            sol1(t1.left)
        if t1.right:
            sol1(t1.right)
        if not (t1.left or t1.right):
            leafs1.append(t1.val)

    def sol2(t2: TreeNode):
        nonlocal leafs2

        if t2.left:
            sol2(t2.left)
        if t2.right:
            sol2(t2.right)
        if not (t2.left or t2.right):
            leafs2.append(t2.val)

    sol1(root1)
    sol2(root2)

    return leafs1 == leafs2

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def search_with_parent(self, root: TreeNode, key: int) -> tuple[Optional[TreeNode]]:
        node = root
        par = None

        while node.val != key:
            if key < node.val:
                if node.left:
                    par = node
                    node = node.left
                else:
                    return None, None
            else:
                if node.right:
                    par = node
                    node = node.right
                else:
                    return None, None

        return node, par

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        node, par = self.search_with_parent(root, key)
        biggest = None

        if not node:
            return root

        if not node.left and not node.right and par:

            if par.left and par.left.val == key:
                par.left = None
            elif par.right and par.right.val == key:
                par.right = None

        elif bool(node.left) ^ bool(node.right):

            if par and par.left and par.left.val == key:
                if node.left:
                    par.left = node.left
                else:
                    par.left = node.right
            elif par and par.right and par.right.val == key:
                if node.left:
                    par.right = node.left
                else:
                    par.right = node.right
            else:
                if node.left:
                    return node.left
                else:
                    return node.right

        else:
            prev_biggest = None
            biggest = node.left

            while biggest and biggest.right:
                prev_biggest = biggest
                biggest = biggest.right

            if biggest:
                node.val, biggest.val = biggest.val, node.val

            if prev_biggest:
                if biggest.left:
                    prev_biggest.right = biggest.left
                else:
                    prev_biggest.right = None
            else:
                if biggest and biggest.left:
                    node.left = biggest.left
                else:
                    node.left = None

        if key == root.val:
            return biggest
        return root

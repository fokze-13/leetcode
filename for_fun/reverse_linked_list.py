from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, next_node: Node | None = None):
        self.val = val
        self.next_node = next_node


def sol(h: Node) -> Node:
    if h.next_node is None:
        return h

    a = h
    b = a.next_node
    c = b.next_node

    a.next_node = None

    while c is not None:
        a.next_node = None
        b.next_node = a

        a = b
        b = c
        c = c.next_node

    b.next_node = a

    return b

def node_as_list(h: Node) -> list:
    res = []

    while h is not None:
        res.append(h.val)
        h = h.next_node

    return res


h1 = Node(1)
h1.next_node = Node(2)
h1.next_node.next_node = Node(3)


print(node_as_list(h1))
print(node_as_list(sol(h1)))

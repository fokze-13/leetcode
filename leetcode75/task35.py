from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sol(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    if not head.next:
        return head

    prev = head
    curr = head.next
    nxt = head.next.next

    prev.next = None
    while nxt:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next
    curr.next = prev

    return curr
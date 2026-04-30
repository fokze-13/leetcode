from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sol(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return

    one = two = head
    prev = None

    while two and two.next:
        prev = one
        one = one.next
        two = two.next.next

    prev.next = one.next

    return head
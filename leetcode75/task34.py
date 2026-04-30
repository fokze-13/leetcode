from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sol(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    odd = head
    even = even_head = head.next

    while odd and odd.next and even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head

    return head
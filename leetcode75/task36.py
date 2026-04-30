from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: Optional[ListNode]) -> int:
    first = head
    second = head.next

    first_half = []

    while second and second.next:
        first_half.append(first.val)
        first = first.next
        second = second.next.next
    first_half.append(first.val)

    m = first_half[-1]

    for i in range(len(first_half) - 1, -1, -1):
        first = first.next
        first_half[i] += first.val

        if first_half[i] > m:
            m = first_half[i]

    return m

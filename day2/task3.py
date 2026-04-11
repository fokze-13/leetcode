class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(head: ListNode) -> list[int]:
    stack = []
    ans = []
    i = 0

    while head is not None:
        ans.append(0)
        if not stack or stack[-1][0] >= head.val:
            stack.append((head.val, i))
        else:
            while stack and head.val > stack[-1][0]:
                pop = stack.pop()
                ans[pop[1]] = head.val
            stack.append((head.val, i))
        head = head.next
        i += 1

    return ans


a = [1,7,5,1,9,2,5,1]
h = h_head = ListNode()
for i in a:
    h.val = i
    h.next = ListNode()
    h = h.next

print(sol(h_head))

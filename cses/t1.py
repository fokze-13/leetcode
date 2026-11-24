# import sys
# from collections import deque
#
# def main():
#     inp = sys.stdin.buffer.read().split()
#
#     n, k = int(inp[0]), int(inp[1])
#     d = deque(range(1, n + 1))
#
#     k_iter = k % n
#
#     out = []
#
#     cnt = 0
#
#     while d:
#         elem = d.popleft()
#
#         if cnt != k_iter:
#             d.append(elem)
#             cnt += 1
#
#         else:
#             out.append(str(elem))
#
#             if len(out) == n:
#                 break
#
#             k_iter = k % (n - len(out))
#             cnt = 0
#
#     sys.stdout.write(" ".join(out))
#
# main()

# n, k = map(int, input().split())
#
# a = list(range(1, n + 1))
#
# f = 1
#
# cnt = 1
#
# out = []
#
# k_iter = k % n
#
# while f:
#     f = 0
#
#     for i in range(n):
#         if a[i] != -1:
#             f = 1
#
#             if cnt == k_iter + 1:
#                 cnt = 1
#                 out.append(a[i])
#
#                 a[i] = -1
#
#                 if len(out) == n:
#                     f = 0
#                     break
#                 else:
#                     k_iter = k % (n - len(out))
#             else:
#                 cnt += 1
#
# print(*out)

import sys

def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    tree = [i & -i for i in range(n + 1)]
    LOG = 1 << n.bit_length()
    out = []
    pos = 0
    for m in range(n, 0, -1):
        pos = (pos + k) % m
        need = pos + 1
        idx = 0
        step = LOG
        while step:
            nxt = idx + step
            if nxt <= n:
                t = tree[nxt]
                if t < need:
                    idx = nxt
                    need -= t
                else:
                    tree[nxt] = t - 1
            step >>= 1
        out.append(idx + 1)
    sys.stdout.write(" ".join(map(str, out)))

main()

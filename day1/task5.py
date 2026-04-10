from collections import deque

f = deque(map(int, input().split()))
s = deque(map(int, input().split()))


i = 1
while i < 1e6:
    c1 = f.popleft()
    c2 = s.popleft()

    if c1 > c2:
        if c1 == 9 and c2 == 0:
            s.append(c1)
            s.append(c2)
        else:
            f.append(c1)
            f.append(c2)
    else:
        if c2 == 9 and c1 == 0:
            f.append(c1)
            f.append(c2)
        else:
            s.append(c1)
            s.append(c2)

    if not f:
        print(f"second {i}")
        break
    if not s:
        print(f"first {i}")
        break

    i += 1
else:
    print("botva")

from bisect import bisect_right


n = int(input())
a = list(map(int, input().split()))

mins = []

for elem in a:
    r = bisect_right(mins, elem)

    if r == len(mins):
        mins.append(elem)
    else:
        mins[r] = elem

print(len(mins))

n = int(input())
a = int(input())
v = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * n
dp[a] = 0

queue = {a}
visited = {a}

while queue:
    new_queue = set()

    for elem in queue:
        for i in range(n):
            if i not in visited:
                new_queue.add(i)

            if v[elem][i] > 0:
                dp[i] = min(dp[i], dp[elem] + v[elem][i])

            visited.add(i)

    queue = new_queue

print(dp)

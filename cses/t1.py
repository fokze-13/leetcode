import sys
from collections import Counter

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    MOD = 10**9 + 7

    ans = 1
    for c in Counter(data[1:n+1]).values():
        ans = ans * (c + 1) % MOD

    print((ans - 1) % MOD)

main()
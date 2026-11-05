import sys

def main():
    data = sys.stdin.buffer.read().split()
    a = sorted(map(int, data[1::2]))
    b = sorted(map(int, data[2::2]))

    j = 0
    mx = 0
    for i, x in enumerate(a):
        while b[j] < x:
            j += 1
        if i + 1 - j > mx:
            mx = i + 1 - j
    print(mx)

main()
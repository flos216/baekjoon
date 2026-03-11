import sys

a = int(sys.stdin.readline())

for i in range(0, a, +1):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)
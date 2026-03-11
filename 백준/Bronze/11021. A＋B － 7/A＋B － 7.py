import sys

a = int(sys.stdin.readline())

for i in range(1, a+1, +1):
    x, y = map(int, sys.stdin.readline().split())
    print("Case #{0}".format(i), end= ": ")
    print(x+y)
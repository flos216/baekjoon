sum = int(input())
n = int(input())
c = 0

for i in range(0, n, +1):
    a, b = map(int, input().split())
    c += a*b
if c == sum:
    print("Yes")
else:
    print("No")
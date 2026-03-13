n, m = map(int, input().split())
a=[0]*n

for x in range(0, n):
    a[x] = x+1

for l in range(0, m):
    i, j = map(int, input().split())
    a[i-1], a[j-1] = a[j-1], a[i-1]
    
for q in range(n):
    print(a[q], end=" ")
    
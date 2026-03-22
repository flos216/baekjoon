n, m = map(int, input().split())
a=[0]*n

for q in range(n):
    a[q]=q+1

for x in range(m):
    i, j = map(int, input().split())
    a[(i-1):j] = a[(i-1):j][::-1]

for w in range(n):
    print(a[w], end=" ")

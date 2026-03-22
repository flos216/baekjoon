a = int(input())
b = list(map(int, input().split()))
c=[0]*a
d=0

for i in range(len(b)):
    c[i]=((b[i]/max(b))*100)
    d=d+c[i]

print(d/len(b))
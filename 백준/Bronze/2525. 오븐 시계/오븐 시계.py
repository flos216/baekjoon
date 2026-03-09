a , b = map(int, input().split())
c = int(input())
d = b + c
e = 0

if a < 23:
    e = a + (d // 60)
    b = d % 60
if e > 23:
    e = e - 24
b = d % 60
        
print(e, b)
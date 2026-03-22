a=[]*10

for i in range(10):
    c=int(input())
    a.append(c%42)
    
a = set(a)
print(len(a))
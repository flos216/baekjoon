a = int(input())
b = [0]*a
sum = 0

b = list(map(int, list(input())))

for i in range(a):
    sum = sum + b[i]
print(sum)
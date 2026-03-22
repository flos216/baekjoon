a = input()
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0

for ch in a:
    for i in b:
        if ch in i:
            sum += b.index(i) + 3
            break
print(sum)
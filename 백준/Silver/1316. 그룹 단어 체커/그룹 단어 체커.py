a = int(input())

for _ in range(a):
    word=[]
    for b in input():
        if b not in word:
            word.append(b)
        else:
            if word[-1] != b:
                a -= 1
                break
print(a)
            
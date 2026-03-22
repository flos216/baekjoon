a = [0]*26
a = list(input())
b = [chr(c) for c in range(97,123)]

for i in range(len(b)):
        if b[i] in a:
            print(a.index(b[i]), end=" ")
        else:
            print("-1", end=" ")
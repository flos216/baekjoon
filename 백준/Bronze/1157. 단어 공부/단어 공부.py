word = input().upper()
unique = list(set(word))
cnt = []

for ch in unique:
    cnt.append(word.count(ch))
    
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(unique[cnt.index(max(cnt))])
    
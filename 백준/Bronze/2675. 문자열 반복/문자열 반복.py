a = int(input())

for i in range(a):
    r, s = input().split()
    r = int(r)
    
    for ch in s:
        print(ch * r, end="")
    print()
        
        

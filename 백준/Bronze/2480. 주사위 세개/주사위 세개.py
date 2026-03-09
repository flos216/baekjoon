a, b, c = map(int, input().split())
d = 0

if a==b and b==c:
    d = 10000+a*1000
elif a==b and b!=c:
    d = 1000+a*100
elif b==c and a!=b:
    d = 1000+b*100
elif a==c and c!=b:
    d = 1000+a*100
elif a!=b!=c:
    if a>b>c:
        d = a*100
    elif a>c>b:
        d = a*100
    elif b>a>c:
        d = b*100
    elif b>c>a:
         d = b*100
    elif c>a>b:
         d = c*100
    elif c>b>a:
          d = c*100
        
print(d)
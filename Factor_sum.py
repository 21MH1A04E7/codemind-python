def fun(n):
    p=0
    for i in range(1,n+1):
        if n%i==0:
            p+=i
    return p
a=list(map(int,input().split(',')))
b=[]
for i in a:
    x=fun(i)
    if x in a:
        b.append(i)
b.sort()
if len(b)==0:
    print(-1)
else:
    print(*b)
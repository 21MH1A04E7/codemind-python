n=int(input())
a=0
b=1
while a<=n:
    i=a
    c=a+b
    b=a
    a=c
    s=a
x=abs(n-i)
y=abs(n-s)
if x<y:
    print(i)
elif x==y:
    print(i,s)
else:
    print(s)
    
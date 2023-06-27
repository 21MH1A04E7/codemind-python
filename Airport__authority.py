n=int(input())
d=0
a=[]
for i in range(n):
    a.append(int(input()))
p=int(input())
for i in a:
    if(i<=p):
        d=d+1
    else:
        d=d+2
print(d)

a,b=map(int,input().split())
if 1==abs(a-b):
    print("Yes")
elif b==10 and a==1 or(a==10 and b==1):
    print("Yes")
else:
    print("No")
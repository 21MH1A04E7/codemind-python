n=int(input())
for i in range(n-1,-1,-1):
    for j in range(-1,i):
        print(chr(i+65),end=" ")
    print()
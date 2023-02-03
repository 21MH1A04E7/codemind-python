str=input()
word=""
c=1
for i in range(len(str)):
    if str[i]==' ':
        s='z'
        for i in range(len(word)):
            s=min(s,word[i])
        if c:
            print(s,end=" ")
            c=0
        word=""
    else:
        word+=str[i]
l='A'
s='z'
for i in range(len(word)):
    s=min(s,word[i])
    l=max(l,word[i])
if c:
    print(s,end=" ")
print(l,end=" ")
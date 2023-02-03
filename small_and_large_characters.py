str=input()
word=""
for i in range(len(str)):
    if str[i]==' ':
        s='z'
        l='A'
        for i in range(len(word)):
            s=min(s,word[i])
            l=max(l,word[i])
        print(s,l,end=" ")
        word=""
    else:
        word+=str[i]
s='z'
l='A'
for i in range(len(word)):
    s=min(s,word[i])
    l=max(l,word[i])
print(s,l,end="")
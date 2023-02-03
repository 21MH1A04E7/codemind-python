str=input()
word=""
small=large=0
for i in range(len(str)):
    if str[i]==' ':
        s='z'
        l='A'
        for i in range(len(word)):
            s=min(s,word[i])
            l=max(l,word[i])
        small+=ord(s)
        large+=ord(l)
        word=""
    else:
        word+=str[i]
s='z'
l='A'
for i in range(len(word)):
    s=min(s,word[i])
    l=max(l,word[i])
small+=ord(s)
large+=ord(l)
print(abs(small-large),end="")
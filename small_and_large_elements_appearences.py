str=input()
s='z'
l='A'
for i in range(len(str)):
    if str[i]==' ':
        continue
    else:
        s=min(s,str[i])
        l=max(l,str[i])
small=large=0
for i in range(len(str)):
    if str[i]==s:
        small+=1
    elif str[i]==l:
        large+=1
print(s,small,l,large)
        
        

str=input()
c=0
for i in range(0,len(str)):
    if (str[i]>='a'and str[i]<='z') or (str[i]>='A' and
    str[i]<='Z') or str[i]==' ':
        continue
    else:
        c+=1
print(c)
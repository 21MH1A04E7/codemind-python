str=input()
c=0
for i in range(0,len(str)):
    if (str[i]>='a'and str[i]<='z') :
        c+=1
print(c)
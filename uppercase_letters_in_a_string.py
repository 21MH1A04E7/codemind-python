str=input()
c=0
for i in range(0,len(str)):
    if (str[i]>='A' and str[i]<='Z') :
        c+=1
print(c)
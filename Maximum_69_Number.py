n=int(input())
k=n
a=[]
while k:
    d=k%10
    a.append(d)
    k//=10
a=a[::-1]    
for i in range(len(a)):
    if a[i]==6:
        a[i]=9
        break
r=0    
for i in range(len(a)):
    r=r*10+a[i]
print(r)    
    
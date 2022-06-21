x=input()
x=x.split()
k=2
a=[]
for i in x:
    if k%2==0:
        a.append(i[::-1])
    k+=1
k=2
b=0
for i in range(len(x)):
    if k%2==0:
        x[i]=a[b]
        b+=1
    k+=1    
print(*x)        
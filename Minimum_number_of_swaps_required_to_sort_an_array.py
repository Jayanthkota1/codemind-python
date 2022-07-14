n=int(input())
a=list(map(int,input().split()))
k=list(a)
c=0
for i in range(n):
    m=min(k)
    d=a.index(m)
    if(d==i):
        k.remove(m)
        continue
    else:
        a[i],a[d]=a[d],a[i]
        c+=1
    k.remove(m)    
print(c)    
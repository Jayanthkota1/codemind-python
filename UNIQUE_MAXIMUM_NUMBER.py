n=int(input())
a=list(map(int,input().split()))
c=0
k=0
b=[]
for i in range(n):
    c=0
    if a[i]==-1:
        continue
    for j in range(i+1,n):
        if a[i]==a[j]:
            a[j]=-1
            c+=1
    if c==0:
        k=1
        b.append(a[i])
if k==1:
    print(max(b))
else:
    print('-1')
    
        
        
n,m=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n):
    c=0
    c=c+a[i]
    if(c==m):
        s+=1
    for j in range(i+1,n):
        c=c+a[j]
        if c==m:
            s+=1
print(s)            
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    c=0
    for j in range(i+1,n):
        if a[i]==a[j]:
         a[j]=-1
         c+=1
    if c==1:
        print(a[i])
                
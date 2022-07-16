n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if a[i]==1:
        s=s+a[i]
    for j in range(1,a[i]):
        if j*j==a[i]:
            s=s+a[i]
print(s)            
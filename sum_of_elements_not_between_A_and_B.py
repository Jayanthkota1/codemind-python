k=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
s=0
for i in a:
    if i>=m and i<=n:
        continue
    else:
        s=s+i
print(s)        
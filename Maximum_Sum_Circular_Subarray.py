n=int(input())
l=list(map(int,input().split()))
s=0
l.append(l[0])
m=[]
for i in range(n):
    m.append(l[i])
for i in range(n+1):
    c=0
    for j in range(i,n+1):
        if i==0 and j==n:
            continue
        c=c+l[j]
        m.append(c)
print(max(m))
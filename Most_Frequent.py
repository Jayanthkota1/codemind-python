n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
c=[]
for i in range(n):
    c.append(a.count(a[i]))
k=c.index(max(c))
print(a[k])
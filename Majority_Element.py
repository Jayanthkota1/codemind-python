n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(a.count(i))
k=max(b)
f=b.index(k)
print(a[f])
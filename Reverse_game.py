n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    k=i
    r=0
    while(k):
        d=k%10
        r=r*10+d
        k//=10
    c.append(r)
print(*c)        
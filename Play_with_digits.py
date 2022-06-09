n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    k=i
    r=0
    while(k):
        d=k%10
        r=r+d
        k//=10
    c=c+r
print(c)    
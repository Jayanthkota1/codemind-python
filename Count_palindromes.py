n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    k=i
    r=0
    while(k):
        d=k%10
        r=r*10+d
        k//=10
    if(i==r):
        c+=1
print(c)        
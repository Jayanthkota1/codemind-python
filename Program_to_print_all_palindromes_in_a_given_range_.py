a=int(input())
b=int(input())
r=0
for i in range(a,b+1):
    n=i
    r=0
    while(n):
        d=n%10
        r=r*10+d
        n//=10
    if(i==r):
        print(i,end=' ')
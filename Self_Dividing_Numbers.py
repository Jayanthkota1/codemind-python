a=int(input())
b=int(input())
c=0
c1=0
for i in range(a,b+1):
    n=i
    c=0
    c1=0
    while n:
        d=n%10
        c+=1
        n//=10
        if d==0:
            continue
        elif i%d==0:
            c1+=1
    if c==c1:
        print(i,end=' ')
n=int(input())
a=list(map(int,input().split()))
s=0
c=0
g=0
for i in a:
    if i==a.count(i):
        a.remove(i)
        s=s+i
        g=1
        c+=1
if g==0:
    print(-1)
else:    
    print('{:.2f}'.format(s/c))
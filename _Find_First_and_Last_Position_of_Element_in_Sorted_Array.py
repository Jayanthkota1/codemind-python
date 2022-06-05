n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
m=int(input())
c=0
for i in range(n):
    if a[i]==m:
        print(i,end=' ')
        break
else:
    c=1
    print('-1 -1')
for i in range(n-1,-1,-1):
    if a[i]==m:
        print(i,end=' ')
        break
    
        
    
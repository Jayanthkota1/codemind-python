n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    s=0
    while a[i]:
        d=a[i]%10
        s+=1
        a[i]//=10
    if s%2==0:
        k+=1
print(k)    
    
        
        
n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if i%2==0:
        s=s+a[i]
    if i%2!=0:
        s1=s1+a[i]
if s-s1==0:
    print("YES")
else:
    print("NO")
    
        
        
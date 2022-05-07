a=int(input())
for i in range(a-1,1,-1):
 k=i
 rev=0
 while(i):
    d=i%10
    rev=rev*10+d
    i=i//10
 if rev == k:
   break
for j in range(a+1,a+2000):
 p=j
 r=0
 while(j):
    d=j%10
    r=r*10+d
    j=j//10
 if r == p:
   break    
if abs(a-k) == abs(a-p):
    print(k,p)
elif abs(a-k) < abs(a-p):
    print(k)
else:
    print(p)
 
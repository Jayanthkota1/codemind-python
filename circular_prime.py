def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
k=int(input())
c=0
r=0
if prime(k):
    n=k
    while(n):
        d=n%10
        n=n//10
        if d==0:
            c+=1
        r=r*10+d
    if prime(r) and c==0:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
      
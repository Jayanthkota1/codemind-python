def prime(n):
    for i in range(2,n):
        if n%i==0:
            return True
    else:
        return False
n=int(input())
c=1
for i in range(1,n+1):
    if prime(i) and n%i==0:
        c+=1
print(c)        
        
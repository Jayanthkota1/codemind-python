n=int(input())
k=n
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1:
            print(k,end=" ")
        else:
            print("",end=" ")
    k-=1
    print()
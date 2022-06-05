n=int(input())
a=list(map(int,input().split()))
k=a[::-1]
a=sorted(a)
if a==k:
    print("yes")
else:
    print("no")
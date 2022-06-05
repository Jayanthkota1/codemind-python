n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
for i in a:
    if i<1:
        a.remove(i)
        a.append(i)
k=1        
for i in range(n):
    if k!=a[i]:
        print(k)
        break
    k+=1
    
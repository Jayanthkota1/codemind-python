n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    s=0
    for j in range(n):
        if a[i]>a[j]:
            s+=1
    print(s,end=' ')        
    
    
        
        
x=input()
b=x.split()
c=set(b[0])
a=[]
for i in c:
    k=0
    for j in b:
        if i in j:
            k+=1
    if k==len(b):
        print(i)
        break
else:
    print('-1')
        
            
x=input()
x=x.lower()
b=x.split()
c=list(b[0])
f=0
a=[]
for i in c:
    k=0
    for j in b:
        if i in j:
            k+=1
    if k==len(b):
        f+=1
print(f)
        
            
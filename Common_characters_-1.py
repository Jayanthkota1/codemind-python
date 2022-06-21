x=input()
x=x.lower()
b=x.split()
c=list(b[0])
f=0
m=0
a=[]
for i in c:
    k=0
    for j in b:
        if i in j:
            k+=1
    if k==len(b):
        m=1
        print(i,end='')
if(m!=1):
    print('-1')
            
x=input()
y=input()
a=x.split()
b=y.split()
c=0
for i in a:
    if i in b:
        if(b.count(i)==1 and a.count(i)==1):
            c+=1
print(c)            
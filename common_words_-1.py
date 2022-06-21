x=input()
y=input()
x=x.lower()
y=y.lower()
x=x.split()
y=y.split()
c=0
for i in x:
    if i in y:
        c+=1
print(c)        
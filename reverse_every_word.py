x=input()
x=x.split()
a=[]
for i in x:
    a.append(i[::-1])
print(*a)    
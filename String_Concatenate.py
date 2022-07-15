s=input()
s1=input()
k=s+s1
a=[]
for i in k:
    a.append(ord(i))
a=sorted(a)
for i in a:
    print(chr(i),end='')
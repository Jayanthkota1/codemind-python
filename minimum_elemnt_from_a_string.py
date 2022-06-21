x=input()
a1=999
a2=999
for i in x:
    if ord(i)>=97:
        if a1>ord(i):
            a1=ord(i)
    if a2>ord(i):
        a2=ord(i)
if abs(a1-97)<=abs(a2-65):
    print(chr(a1))
else:
    print(chr(a2))
        
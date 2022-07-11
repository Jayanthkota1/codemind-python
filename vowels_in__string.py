s=input()
s=s.split()
a='aeiouAEIOU'
b=''
c=0
max=0
for i in s:
    c=0
    for j in i:
        if j in a and j not in b:
            b=b+j
for i in b:
    print(i,end=' ')
            
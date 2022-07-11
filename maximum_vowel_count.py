s=input()
s=s.lower()
s=s.split()
a='aeiou'
c=0
max=0
for i in s:
    c=0
    for j in i:
        if j in a:
            c+=1
    if c>max:
        max=c
print(max)        
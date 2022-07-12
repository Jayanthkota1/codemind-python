s=input()
s=s+' '
min=999
max=0
for i in s:
    if i==' ':
        print(chr(min),chr(max),end=' ')
        max=0
        min=999
        continue
    if max<ord(i):
        max=ord(i)
    if min>ord(i):
        min=ord(i)
    
s=input()
s1=input()
s=s.lower()
s1=s1.lower()
for i in s:
    if i in s1:
        continue
    else:
        print("False")
        break
else:
    print("True")
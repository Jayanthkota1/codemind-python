n=int(input())
#print(n)
max=0
min=0
for i in range(0,n+1):
 if 2**i<=n:
     max=i
     #print(max)
     #print(2**max)
for j in range(n+1):
 if 2**j>=n:
     min=j
     break
if abs(n-(2**max))<=abs(n-(2**min)):
    print(abs(n-(2**max)))
else:
    print(abs(n-(2**min)))
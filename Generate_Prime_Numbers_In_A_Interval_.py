a=int(input())
b=int(input())
if a<9:
 print(2)
 print(3)
 print(5)
 print(7)
 a=10
for i in range(a,b+1):
  
  for j in range(2,a):
   if i%j==0:
    break
  else:
    print(i)
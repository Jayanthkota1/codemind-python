n=int(input())
c=0
rev=0
while(n!=0):
 d=n%10
 c+=1
 rev=rev*10+d
 n=n//10
if(c==10):
 k=rev%10
 if(k==0):
     print("Invalid")
 else:
     print("Valid")
else:
    print('Invalid')
 
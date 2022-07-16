t=int(input())
for i in range(t):
    n=input()
    r=0
    d=n[::-1]
    e=len(d)
    if(n==d):
        if (e%2==0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
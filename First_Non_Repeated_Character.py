t=int(input())
for i in range(t):
    a=int(input())
    s=input()
    for i in s:
        if s.count(i)==1:
            n=1
            print(i)
            break
    else:
        print(-1)
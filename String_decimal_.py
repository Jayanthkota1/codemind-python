t=int(input())
for i in range(t):
    s=input()
    for i in s:
        if i.isalpha():
            print("False")
            break
    else:
        print("True")
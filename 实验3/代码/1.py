n = int(input("please enter the number："))
m=0
if n<=0:
    print("wrong")
else:
    for i in range(2,n+1):
        j = 2
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            m=m+i
    print(m)
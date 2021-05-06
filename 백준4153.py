while True:
    A=[]
    a,b,c = map(int,input().split())
    A.append(a)
    A.append(b)
    A.append(c)
    A.sort()
    if a==0 and b==0 and c==0:
        break
    else:
        if A[0]**2+A[1]**2==A[2]**2:
            print("right")
        else:
            print("wrong")
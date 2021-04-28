b=[]
while True:
    N = int(input())
    M = 2*N
    if N==0:
        for i in b:
            print(i)
        exit()
    count=0
    a = [False,False] + [True]*(M-1)
    primes=[]
    for i in range(2,M+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, M+1, i):
                a[j] = False
    for i in primes:
        if i>N:
            count+=1 
    b.append(count)


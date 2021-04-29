'''
import itertools 
t=int(input())
while t>0:
    t-=1
    M = int(input())
    a = [False,False] + [True]*(M-1)
    primes=[]
    for i in range(2,M+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, M+1, i):
                a[j] = False
    if M/2 in primes:
        print(M//2,M//2)
    else:
        c = []
        d = {}
        nPr = itertools.combinations(primes, 2)
        for i in nPr:
            if sum(i)==M:
                c.append(i)
        for w in range(len(c)):
            d[w]=abs(c[w][0]-c[w][1])
        list(set(d))
        for w in range(len(c)):
            if min(d.values())==abs(c[w][0]-c[w][1]) :
                print(c[w][0],c[w][1])
 '''   
'''
import itertools 
t=int(input())
while t>0:
    t-=1
    M = int(input())
    a = [False,False] + [True]*(M-1)
    primes=[]
    for i in range(2,M+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, M+1, i):
                a[j] = False
    if M/2 in primes:
        print(M//2,M//2)
    else:
        c = []
        d = []
        nPr = itertools.combinations(primes, 2)
        for i in nPr:
            if sum(i)==M:
                c.append(i)
        for i in c[-1]:
            print(i, end=' ')
        print()
        '''
sosu = [0 for i in range(10001)]
sosu[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        sosu[j] = 1
t = int(input())
for i in range(t):
    a = int(input())
    b = a // 2
    for j in range(b, 1, -1):
        if sosu[a - j] == 0 and sosu[j] == 0:
            print(j, a - j)
            break
        
        
    
        


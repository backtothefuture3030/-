
'''
M,N = map(int,input().split())

for i in range(M,N+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
'''

N,M = map(int,input().split())
a = [False,False] + [True]*(M-1)
primes=[]
for i in range(2,M+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, M+1, i):
        a[j] = False
for i in primes:
    if i>=N:
        print(i)    

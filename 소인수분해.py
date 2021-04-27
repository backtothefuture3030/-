'''
N = int(input())
M = N
W = N
a = []
total=0
for i in range(2,N):
    if N%i==0:
        total+=1

if total==0:
    print(N)
    exit()
if N>=100:
    for i in range(1,int(N**(1/2))):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2  :
            a.append(j)

else:
    for i in range(1,N+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2  :
            a.append(j)
b = []
for i in a:
    while N!=1:
        N/=i
        M//=i
        if N*i == M*i:
            b.append(i)
        else:
            N*=i
            M=N
            break

if W>=100 and len(b)==1:
    b.append(W//b[0])
for i in b:
    print(i)
'''
'''
N = int(input())
M = N
a = []
for i in range(1,N+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        a.append(j)

b=[]
for i in a:
    while N!=1:
        N/=i
        M//=i
        if N*i == M*i:
            b.append(i)
        else:
            N*=i
            M=N
            break
for i in b:
    print(i)

'''
'''
N = int(input())
M = N
W = N
a = []
total=0
for i in range(1,N+1):
    if N%i==0:
        total+=1
if total==2:
    print(N)
    exit()

for i in range(1,int(N**(1/2))+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2  :
        a.append(j)
b = []
for i in a:
    while N!=1:
        N/=i
        M//=i
        if N*i == M*i:
            b.append(i)
        else:
            N*=i
            M=N
            break

if len(b)==1:
    b.append(W//b[0])
for i in b:
    print(i)
    '''
n=int(input())
p=2
while True:
  if n==1: 
      break
  if n%p: 
      p+=1
  else: 
      print(p); n//=p
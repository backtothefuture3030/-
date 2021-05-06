a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

A = []
B = []
A.append(a)
A.append(c)
A.append(e)
B.append(b)
B.append(d)
B.append(f)
for i in A:
    if A.count(i) == 1:
        print(i, end= ' ')
for i in B:
    if B.count(i) == 1:
        print(i)
        


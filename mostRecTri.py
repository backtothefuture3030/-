

a={}
for w in range(1,1001):
    count=0
    for i in range(1,((w+1)//2+1)//2+1):
        for j in range(1,(w+1)//2+1):
            q=w-i-j
            if i**2+j**2==q**2:
                count+=1
    if count!=0:
        a[w]=count
print(max(a,key=a.get))


import math
def Tri(n):
    a = 0
    c = 0.0
    p =n/2
    _list = []
    while a < p:
        a += 1
        for b in range(a,int(p-a)+1):
            c = math.sqrt(a*a + b*b)
            if c % 1 == 0:
                _list.append( a+b+c )
    return int(max(set(_list),key=_list.count))


print (Tri(1000))




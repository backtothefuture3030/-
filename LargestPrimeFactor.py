
def Factors(n):
    count = 2
    while count < n:
        if n % count  ==  0:
            Factors(n/count)
            return 0
        count += 1
    print (n)


Factors(600851475143)




'''
a=600851475143

b=[]
c=[]

for i in range(2,a+1):
    if a%i==0:
        b.append(i)
for q in b:
    count=0
    for j in range(1,q+1):
        if q%j==0:
            count+=1
            if count==2 and j==q:
                c.append(q)
        else:
            pass

print(c)
'''




'''
# 7의배수, 10의자리 이상의 소수.
count=0
for i in range(1,1501):
    if i%7==0:
        count+=1
print(count)
count1=0

for i in range(1,1500):
    total=0
    for j in range(1,i):
        if i%j==0:
            total+=1
    if total==1:
        count1+=1
print(count1)
'''
'''
a=[1,2,3,4,5,6,8,9]

while len(a)<=1500:
    for i in range(10,1501):
        for j in range(2,i):
            if i%j!=0 or i%7!=0:
                a.append(i)
    a.sort()
    list(set(a))
print(a[-1])    

'''

a=9
b=[1,2,3,4,5,6,8,9]
c=[]

while len(b)<=1500:
    a+=1
    count=0
    for i in range(2,a):
        if a%i==0 and a%7!=0:
            b.append(a)
            count+=1
        elif a%7==0:
            c.append(a)          # 소수, 7의배수가 들어있는 c
        elif a%i==0:
            count+=1
    if count==0:
        c.append(a)
    c.sort()
    c=list(set(c))            
    b.sort()
    b = list(set(b))
    '''
    for j in b:                        # 나눠진 수중에 소수가 끼어있는지 판단
        for q in range(2,j):
            if j%q==0:
                if j/q in c:
                    b.remove(j)
    '''        
            
print(b[-1])



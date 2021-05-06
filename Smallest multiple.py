# 3^2 2^3 7 5 
# 소수, 그리고 20안의 최대로큰 2와 3의 제곱수

a=[]
for i in range(1,21):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        a.append(i)
a.remove(2)
a.remove(3)
count=0
while True:
    count+=1
    if 2**count>=10:
        a.append(2**count)
        break
count=0
while True:
    count+=1
    if 3**count>=7:
        a.append(3**count)
        break
total=1
for i in a:
    total*=i
print(a)
print(total)














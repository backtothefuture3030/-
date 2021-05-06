a= ['3','30','34','5','9']
b= [3,30,34,5,9]
c= {}
d={}
e=[]
# 9534303  0번째 자리의 숫자를 비교한다 만약 0번쨰 자리가 같은 숫자면 1번째 자리 비교후 1번째 자리가 큰수가 먼저들어간다, 그치만 자리수가 적다면 0번째와 1번째를 비교

k=0
i=0

for j in b:
    c[k]=(int(str(j)[0]))
    if len(str(j))>1:
        d[k] = int((str(j)[1]))
        k+=1
    else:
        d[k]=(int(str(j)[0]))
        k+=1  
print(c)
print(d)



'''
while True:
    for i in a:
        a+=i
    if int(a)
'''
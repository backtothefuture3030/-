
a=int(input("숫자를 입력하세요 : "))
b={}
for i in range(1,a+1):
    for j in range(1,i+1):
        if i*j==a:
            if i==j:
                b[i]=j
            b[i]=j
            b[j]=i
print(b)




from itertools import permutations # 순열 과 조합 툴

n = int(input("곱의 값: "))
m = int(input("이루어진 정수의 수 :"))
c=[]
items=[]
for i in range(1,n+1):
    items.append(str(i))
a = list(map(' '.join,permutations(items,m)))

for i in a:
    w=1
    i = i.split()
    for j in range(len(i)):
        w*=int(i[j])
    if w==n:
        c.append(i)

print(c)



            
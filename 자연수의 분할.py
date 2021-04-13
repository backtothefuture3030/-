import itertools
q = int(input("숫자 입력 : "))
w = list(range(1,q))
n = int(input("쌍 : "))
a=[]
c=[]
result = list(itertools.product((w), repeat=n))  # 중복순열
for i in result:
    total=0
    for j in i:
        total+=int(j)
    if total== q :
        a.append(i)
for i in a:
    c.append(sorted(list(i))) 
print(len(list(set(map(tuple,c)))))
print(list(set(map(tuple,c))))

        





        
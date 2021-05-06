from itertools import combinations
'''
n={}
q = '1123'  # 한개씩 다 쪼개는 방법, 두개씩 쪼개는방법이 전부. 하지만 두개씩 쪼갤때는 쪼갠수가 26을 넘으면 안된다.
a=[]
b=[]
for i , j in enumerate(list(map(chr, range(97,123)))):      # 알파벳 딕셔너리에 저장
    n[str(i+1)]=j

for i in range(len(q)):                 # 하나
    print(n[q[i]], end='')
print()

# 1, 1, 2, 3    11, 2, 3    1, 12, 3    1, 1, 23     11, 23   

if len(q)%2==0:


for i in list(combinations(q,2)):
    a.append(i)


print(a)
for i in range(len(a)):
    b.append(a[i][0]+a[i][1])
print(b)

for i in b:
    a = q.find(i)
    print(n[i], end='')
    w = q.replace(i,"")
    for j in w:
        print(n[j],end='')
    print()
'''




A = 'abcdefghijklmnopqrstuvwxyz'

def itoa(s, n):
    if n == '':
        print(s)
        return None
    itoa(s + A[int(n[0]) - 1], n[1:])  # (' 1', '123')
    if len(n) >= 2 and int(n[0:2]) <= 26:
        itoa(s + A[int(n[0:2]) - 1], n[2:])

itoa('','1123')

print(A[1])
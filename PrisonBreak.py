# 딕셔너리 개념을 이용해서 초기치는 0 열릴때1을 더해 1로 엶을 표현, 닫혀있을때 -1을해서 0은 닫힘
# 딕셔너리 키값을 이용해서 1인값들만 추린다 

prison={}
for i in range(1,121):       
    prison[i]=0

for i in range(1,121):            
    for n in range(1,121):
        if 120>=i*n:
            prison[i*n]+=1
        elif 120<i*n:
            break

total = 0
for i in range(1,121):
    if prison[i]%2==1:
        total+=1
print(total)






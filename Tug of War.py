

from itertools import combinations

def Tug(i):
    w=0
    a=[]
    diff=[]
    if i>100:
        exit()
    while w<i:                          # 숫자 대입받기
        b=int(input("무게를 입력 : "))
        if 1>b or b>450:  # 몸무게 조건
            break
        a.append(b)
        w+=1
    r=i//2
    s=sum(a)/2
    total = combinations(a,r)  # 조합이용해서 경우의수 찾기
    for i in total:
        diff.append(abs(s-sum(i)))
    print(int(s-min(diff)),int(s+min(diff)))
        
Tug(int(input("인원을 입력하세요 : ")))




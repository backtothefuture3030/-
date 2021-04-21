

def num(n):
    a = [2] # n보다 작은 소수들의 리스트
    for i in range(3,n+1):    # 그 수의 소수를 구하는 과정
        count=0
        for j in range(1,n+1):
            if i%j==0:
                count+=1
        if count==2:
            a.append(i)
    return a

def gold():
    b=[]
    n = int(input("2보다 큰 짝수를 입력하세요 : "))
    for i in num(n//2):
        for j in num(n):
            if i+j==n:
                b.append([i,j])
    print(b)


gold()                

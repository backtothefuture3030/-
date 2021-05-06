
n = int(input("홀수인 양수만 입력하세요 : "))
i = 0
while i<n:
    if n==1:
        print('N')
    elif i==1:
        print('N', end='')
        print('N', end=' '*(n-i-2))
        print('N')
    elif 1<i<(n-1):
        print('N', end=' '*(i-1))
        print('N', end=' '*(n-i-2))
        print('N')
    else:
        print('N',end=' '*(n-2))
        print('N')
    i+=1




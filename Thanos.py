import random

def Thanos(a):
    random.shuffle(a)
    if len(a)%2==1:
        b=[len(a)//2,len(a)//2+1]
    else:
        b=[len(a//2)]
    for i in range(random.choice(b)):
        del a[i]
    print(a)

Thanos(list(input("숫자를 입력하세요 : ").split()))
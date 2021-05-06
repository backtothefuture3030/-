import random
import numpy as np

def Sheet():
    count=0
    A=int(input("격자의 가로길이 : "))
    B=int(input("격자의 세로길이 : "))
    a = np.zeros((A,B))
    c = int(input("행 입력 : "))-1  # 시작위치지정
    d = int(input("열 입력 : "))-1
    print(a)
    while True:
        total=0 
        if (c==0 and d==0):  # 좌측 위 아래 끝
            q = random.randrange(0,3)
            if q==0:
                c+=1
            elif q==1:
                c+=1
                d+=1
            elif q==2:
                d+=1
            a[c,d]+=1          # 랜덤의 수가 나온이후 랜덤자리에 1을 넣어줘서 지나갔다는 흔적을 남김
        elif  (c==A-1 and d==0):
            w= random.randrange(0,3)
            if w==0:
                c-=1
            elif w==1:
                c-=1
                d+=1
            elif w==2:
                d+=1
            a[c,d]+=1
        elif (c==0 and d==B-1):  # 우측 위 아래 끝
            z=random.randrange(0,3)
            if z==0:
                d-=1
            elif z==1:
                c+=1
                d-=1
            elif z==2:
                c+=1
            a[c,d]+=1
        elif (c==A-1 and d==B-1):
            r=random.randrange(0,3)
            if r==0:
                c-=1
            elif r==1:
                d-=1
            elif r==2:
                c-=1
                d-=1
            a[c,d]+=1
        elif c==0:     #0번째 줄 
            t = random.randrange(0,5)
            if t==0:
                d-=1
            elif t==1:
                d+=1
            elif t==2:
                c+=1
                d-=1
            elif t==3:
                c+=1
            elif t==4:
                d+=1
                c+=1
            a[c,d]+=1
        elif c==A-1:     # 6번째 줄
            t = random.randrange(0,5)
            if t==0:
                d-=1
            elif t==1:
                d+=1
            elif t==2:
                c-=1
                d-=1
            elif t==3:
                c-=1
            elif t==4:
                d+=1
                c-=1
            a[c,d]+=1
        elif d==0:
            y=random.randrange(0,5)
            if y==0:
                c-=1
            elif y==1:
                c-=1
                d+=1
            elif y==2:
                d+=1
            elif y==3:
                c+=1
            elif y==4:
                c+=1
                d+=1
            a[c,d]+=1
        elif d==B-1:
            y=random.randrange(0,5)
            if y==0:
                c-=1
            elif y==1:
                c-=1
                d-=1
            elif y==2:
                d-=1
            elif y==3:
                c+=1
            elif y==4:
                c+=1
                d-=1
            a[c,d]+=1
        else:
            y=random.randrange(0,8)
            if y==0:
                c-=1
                d-=1
            elif y==1:
                c-=1
            elif y==2:
                c-=1
                d+=1
            elif y==3:
                d-=1
            elif y==4:
                d+=1
            elif y==5:
                c+=1
                d-=1
            elif y==6:
                c+=1
            elif y==7:
                c+=1
                d+=1
            a[c,d]+=1
        count+=1
        for i in range(A):    # 반복문을 통해서 시트안의 자취흔적 조사 
            for j in range(B):
                if a[i,j]>0:
                    total+=1
                    if total==A*B:
                        break
            if total==A*B:
                break
        if total==A*B:
            break
    print(a)
    print(count)
Sheet()

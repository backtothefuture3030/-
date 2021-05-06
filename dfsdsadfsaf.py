

def plus():
    a=[]
    b=[]
    A=input("숫자입력 : ")
    for i in range(len(A)):
        a.append((int(A[i])))
    B = input("숫자입력 : ")
    for i in range(len(B)):
        b.append((int(B[i])))
    if len(a) != len(b):
        if len(a)>len(b):
            for i in range(1,len(b)+1):
                if a[-i]<b[-i]:
                    a[-i]=b[-i]
            for i in a:
                print(i, end='')
        else:
            for i in range(1,len(a)+1):
                if a[-i]>b[-i]:
                    b[-i]=a[-i]
            for i in b:
                print(i, end='')
    else:
        for i in range(1,len(a)+1):
            if a[-i]<b[-i]:
                a[-i]=b[-i]
        for i in a:
            print(i, end='')



def mul():
    a=[]
    b=[]
    c=[]
    total=[]
    A=input("숫자입력 : ")
    for i in range(len(A)):       
        a.append((int(A[i])))
    B = input("숫자입력 : ")
    for i in range(len(B)):
        b.append((int(B[i])))   # 숫자를 받은후 리스트 형식으로 변환



                   # 수의 단위 같을경우
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if b[-i]<a[-j]:
                a[-j]=b[-i]          # 비교
        c.append(list(a))
    for i in range(len(c)):       # 자리수 맞추기
        for j in range(i):
            c[i].append(0)
    for i in range(len(c)-1):
        for j in range(1,len(c[i])+1):
            if c[i][-j]>c[i+1][-j]:
                c[i+1][-j]= c[i][-j] 
    for j in c[-1]:
        print(j, end='')



def Lunar():
    a = input("곱셈선택 : 0 덧셈선택 : 1 : ")
    if a=='0':
        mul()
    elif a=='1':
        plus()
    else:
        print("다시 입력하세요! ")
Lunar()
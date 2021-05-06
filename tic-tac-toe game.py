import numpy as np
import random
data  = np.array([[1,2,3],[4,5,6],[7,8,9]])

def trans():
    a = int(input("선택할 숫자 입력 : "))
    if a-3>3 :
        a-=7
        b=2
    elif a-3>=1:
        a-=4
        b=1
    elif a-3<=0:
        a-=1
        b=0
    if data[b][a] == 10 or data[b][a] ==11 :
        print("선택된 공간입니다")
        trans()
    else:
        data[b][a] = 10
    #print(data)

def com():
    while True:
        c = random.randint(0,2)
        d = random.randint(0,2)
        if data[d][c] == 10 or data[d][c] == 11 :
            print("이미 선택된 공간입니다")
        else:
            data[d][c] = 11
            break
    

def tic():
    while True:
        com()
        if data[0][0]==10 and data[0][1]==10 and data[0][2]==10:
            print("이겼습니다!")
            w=1
            break
        elif data[1][0]==10 and data[1][1]==10 and data[1][2]==10:
            print("이겼습니다!")
            w=1
            break
        elif data[2][0]==10 and data[2][1]==10 and data[2][2]==10:
            print("이겼습니다")
            w=1
            break
        elif data[0][0]==10 and data[1][0]==10 and data[2][0]==10:
            print("이겼습니다")
            w=1
            break
        elif data[0][1]==10 and data[1][1]==10 and data[2][1]==10:
            print("이겼습니다")
            w=1
            break
        elif data[0][2]==10 and data[1][2]==10 and data[2][2]==10:
            print('이겼습니다')
            w=1
            break
        elif data[0][0]==10 and data[1][1]==10 and data[2][2]==10:
            print("이겼습니다")
            w=1
            break
        elif data[0][2]==10 and data[1][1]==10 and data[2][0]==10:
            print("이겼습니다")
            w=1
            break
        if data[0][0]==11 and data[0][1]==11 and data[0][2]==11:
            print("졌습니다!")
            w=1
            break
        elif data[1][0]==11 and data[1][1]==11 and data[1][2]==11:
            print("졌습니다!")
            w=1
            break
        elif data[2][0]==11 and data[2][1]==11 and data[2][2]==11:
            print("졌습니다")
            w=1
            break
        elif data[0][0]==11 and data[1][0]==11 and data[2][0]==11:
            print("졌습니다")
            w=1
            break
        elif data[0][1]==11 and data[1][1]==11 and data[2][1]==11:
            print("졌습니다")
            w=1
            break
        elif data[0][2]==11 and data[1][1]==11 and data[2][0]==11:
            print('졌습니다')
            w=1
            break
        elif data[0][0]==11 and data[1][1]==11 and data[2][2]==11:
            print("졌습니다")
            w=1
            break
        elif data[0][2]==11 and data[1][1]==11 and data[2][0]==11:
            print("졌습니다")
            w=1
            break
        print(data)
        trans()
    



tic()
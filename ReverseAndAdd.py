

def ReverseAndAdd(num):
    count=0
    a =int(num)+int(num[::-1])
    while True:
        if str(a)[::-1]==str(a) and count==0:
            print("%d %d" %(count,a))
            break
        elif str(a)[::-1]==str(a):
            count+=1
            print("%d %d" %(count,a))
            break
        else:
            count+=1
            a+=int(str(a)[::-1])
            
            

ReverseAndAdd(input("회문을 알 숫자를 대입하세요 : "))



